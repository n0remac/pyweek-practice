import math
import arcade
from ..PostProcessingChain import PostProcessingStage
from ..FullscreenQuad import FullscreenQuad
from ..RenderTarget import RenderTarget

#Basic bloom shader
class Bloom(PostProcessingStage):

    #Must match shader
    MAX_WEIGHTS = 15

    def __init__(self, context, taps=5, stdev=2.0, threshold=1.15, power = 1.0):
        super().__init__()
        self.context = context
        self.quad = FullscreenQuad(context)
        self.extract_and_x_blur = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/bloom_extract_xblur.fs'
        )

        self.y_blur_and_combine = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/bloom_yblur_combine.fs'
        )

        self.blurTarget = None
        self.weights = [0.1] * (self.MAX_WEIGHTS )

        self.change_settings(taps,stdev, threshold, power)

    def change_settings(self, taps, stdev, threshold, power):
        if taps < 1:
            taps = 1
        if taps > self.MAX_WEIGHTS:
            taps = self.MAX_WEIGHTS

        #Do fancy math to create gaussian curve weights

        sqrt_term = math.sqrt(2.0 * math.pi * stdev * stdev)
        recp_sqrt_term = 1.0 / sqrt_term

        two_dev_sqr = 2.0 * stdev * stdev

        centerWeight = math.floor(taps / 2)
        for x in range(0,taps):
            pos = x-centerWeight
            weight = recp_sqrt_term * math.exp( -(pos*pos)/two_dev_sqr)
            self.weights[x] = weight


        self.extract_and_x_blur['u_weights'] = self.weights
        self.y_blur_and_combine['u_weights'] = self.weights
        #Apply other settings as needed

        self.extract_and_x_blur['u_weight_count'] = taps
        self.y_blur_and_combine['u_weight_count'] = taps

        #Threshold only needed for extract, power only needed for combine
        self.extract_and_x_blur['u_threshold'] = threshold
        self.y_blur_and_combine['u_power'] = power

        #Both need source, only combine needs xblur (self.tempTarget)
        self.extract_and_x_blur['t_source'] = 0
        self.y_blur_and_combine['t_source'] = 0
        self.y_blur_and_combine['t_xblur'] = 1

    def apply(self, source, target, width, height):
        
        #Ensure we have a buffer and that it is the correct size
        #This effect needs a internal buffer because it needs to run 2 passes,
        #and the final pass needs access to the original input image

        #If you seperate the 2 axis of a gaussian blur you only have to do N+N texture reads instead of N*N
        #Interstingly enough, a non-separated blur in a bloom shader was how I met Free, go figure.
        if self.blurTarget is None:
            self.blurTarget = RenderTarget(self.context, width, height, 'f2')
            #update sizes if target changes
            pixelSizes = (1.0 / width, 1.0 / height)
            self.extract_and_x_blur['u_pixel_size_uv'] = pixelSizes
            self.y_blur_and_combine['u_pixel_size_uv'] = pixelSizes

        elif (self.blurTarget.width != width or self.blurTarget.height != height):
            self.blurTarget.release()
            self.blurTarget = RenderTarget(self.context, width, height, 'f2')
            #update sizes if target changes
            pixelSizes = (1.0 / width, 1.0 / height)
            self.extract_and_x_blur['u_pixel_size_uv'] = pixelSizes
            self.y_blur_and_combine['u_pixel_size_uv'] = pixelSizes

        #bind source to zero, this never moves
        source.bind_as_texture(0)

        #first we draw the x blur to a temp buffer
        self.blurTarget.bind_as_framebuffer()
        self.quad.render(self.extract_and_x_blur)

        #then we draw the y blur to the final image
        target.bind_as_framebuffer()
        self.blurTarget.bind_as_texture(1)
        self.quad.render(self.y_blur_and_combine)