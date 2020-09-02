
import arcade
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad

class TrashChromaticAberration(PostProcessingStage):

    def __init__(self, context, strength):
        super().__init__()
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/TrashChromAberr.fs'
        )

        self.program['t_source'] = 0
        self.program['u_strength'] = strength

    def set_strength(self, strength):
        self.program['u_strength'] = strength

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)

        self.quad.render(self.program)