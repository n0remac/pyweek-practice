import math
import arcade
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad
from Graphics.RenderTarget import RenderTarget
import imgui
#Basic bloom shader
class Bloom(PostProcessingStage):

    #Must match shader
    MAX_WEIGHTS = 45

    def __init__(self, context, taps=5, stdev=2.0, threshold=1.15, power = 1.0):
        super().__init__()

        self._threshold = 0
        self._power = 0
        self._taps = 1 
        self._stdev = 1.0

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

        #Both need source, only combine needs xblur (self.tempTarget)
        self.extract_and_x_blur['t_source'] = 0
        self.y_blur_and_combine['t_source'] = 0
        self.y_blur_and_combine['t_xblur'] = 1

        self.blurTarget = None
        self.weights = [0.1] * (self.MAX_WEIGHTS )

        self.threshold = threshold
        self.power = power
        self.taps = taps
        self.stdev = stdev

        self.change_weights(taps,stdev)

    def change_weights(self, taps, stdev):
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

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self,value):
        self._threshold = max(0.0,value)
        self.extract_and_x_blur['u_threshold'] = self._threshold

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self,value):
        self._power = value
        self.y_blur_and_combine['u_power'] = value

    @property
    def taps(self):
        return self._taps

    @taps.setter
    def taps(self, value):
        self._taps = value
        #Ensure odd
        if self._taps % 2 == 0:
            self._taps += 1
        self.change_weights(self._taps, self._stdev)

    @property
    def stdev(self):
        return self._stdev

    @stdev.setter
    def stdev(self, value):
        self._stdev = value
        self.change_weights(self._taps, self._stdev)

    def show_ui(self):
        super().show_ui()
        self.threshold = imgui.slider_float(f'Threshold##{self.ui_index}', self.threshold, 0.0, 32.0, power=2.0)[1]
        self.power = imgui.slider_float(f'Power##{self.ui_index}', self.power, 0.0, 3.0)[1]
        self.taps = imgui.slider_int(f'Bloom Samples##{self.ui_index}', self.taps, 1, self.MAX_WEIGHTS)[1]       
        self.stdev = imgui.slider_float(f'Blur Radius##{self.ui_index}', self.stdev, 0.0, 10.0)[1]
        if imgui.small_button(f'Compute radius from Samples##{self.ui_index}'):
            self.stdev = self._taps / 6.0
