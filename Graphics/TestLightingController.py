
import arcade
from Graphics.RenderTarget import RenderTarget
from Graphics.FullscreenQuad import FullscreenQuad
from Graphics.PostProcessingChain import PostProcessingStage


class TestLightingController():



    def __init__(self, context):

        self.context = context
        self.lights = []
        self.light_buffer = None
        self.ambient_light = (0.0,0.0,0.0,0.0)
        
        pass

    def create_point_light(self, position, radius, color):
        light = PointLight(self, color, radius, position, self.context)
        self.lights.append(light)
        return light

    def draw_light_buffer(self, context, width, height):

        #Ensure we have a buffer and that it is the correct size
        if self.light_buffer is None:
            self.light_buffer = RenderTarget(context, width, height, 'f2')
        elif (self.light_buffer.width != width or self.light_buffer.height != height):
            self.light_buffer.release()
            self.light_buffer = RenderTarget(context, width, height, 'f2')

        #Bind and clear light buffer to the ambient light color
        self.light_buffer.bind_as_framebuffer()
        self.light_buffer.clear(self.ambient_light)

        #Enable additive blending so that lights stack up instead of overwrite each other
        context.enable_only(context.BLEND)
        context.blend_func = context.BLEND_ADDITIVE

        #draw each light to the light buffer (the light buffer will later be mixed with all the sprites to light them)
        #The project matrix is used to make sure they show up the correct place on-screen when the 'camera' moves
        projection_matrix = context.projection_2d_matrix

        for light in self.lights:
            self.__draw_light(light, projection_matrix)
            pass


    def __draw_light(self, light, projection_matrix):
        light.draw(projection_matrix)
        pass

    def destroy_light(self, light):
        self.lights.remove(light)

    def get_apply_light_stage(self):
        return ApplyLightsInPost(self.context, self)

#base class for all lights
class Light():
    def __init__(self, controller, color):
        self.controller = controller
        self.is_enabled = True
        self.color = color
    
    def destroy(self):
        self.controller.destroy_light(self)

    def draw(self, projection_matrix):
        raise NotImplementedError("Must be implemented in derrived class")

class PointLight(Light):
    shader_program = None
    quad = None

    #Note: Do not directly construct lights, do so from the Light Controller instead
    def __init__(self, controller, color, radius, position, context):
        super(PointLight,self).__init__(controller, color)

        self.radius = radius
        self.position = position

        #load shader if necessary
        if self.shader_program is None:
            self.shader_program = context.load_program(
                vertex_shader='Graphics/Shaders/point_light.vs',
                fragment_shader='Graphics/Shaders/point_light.fs'
            )
        if self.quad is None:
            self.quad = FullscreenQuad(context)

    def draw(self, projection_matrix):
        #set arguments for this light on the shader program
        self.shader_program['lightColor'] = self.color
        self.shader_program['u_radius'] = self.radius
        self.shader_program['u_position'] = self.position
        self.shader_program['u_projection'] = projection_matrix

        #draw it using a quad
        self.quad.render(self.shader_program)
    

#class to apply lighting during post-processing
class ApplyLightsInPost(PostProcessingStage):
    def __init__(self, context, light_controller):
        super().__init__()
        self.light_controller = light_controller

        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/apply_lighting.fs'
        )
        self.program['t_Source'] = 0
        self.program['t_LightBuffer'] = 1


    def apply(self, source, target, width, height):
        target.bind_as_framebuffer()
        source.bind_as_texture(0)
        self.light_controller.light_buffer.bind_as_texture(1)

        self.quad.render(self.program)