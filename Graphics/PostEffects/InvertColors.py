
import arcade
from ..PostProcessingChain import PostProcessingStage
from ..FullscreenQuad import FullscreenQuad

class InvertColors(PostProcessingStage):

    def __init__(self, context):
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/invert_colors.fs'
        )
        self.program['t_source'] = 0

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)

        self.quad.render(self.program)