
import arcade
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad

#Basic tonemap from HDR -> LDR, currently via the simple Reinhard
class Tonemap(PostProcessingStage):

    def __init__(self, context, white_point):
        super().__init__()
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/tonemap.fs'
        )
        self.program['t_source'] = 0
        self.set_white_point(white_point)

    def set_white_point(self,white_point):
        self.program['u_whitePoint_2'] = white_point * white_point

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)

        self.quad.render(self.program)