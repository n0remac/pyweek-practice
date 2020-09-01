
import arcade
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad
import imgui

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
    
        self.white_point = white_point

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)

        self.quad.render(self.program)

    @property
    def white_point(self):
        return self._white_point

    @white_point.setter
    def white_point(self, value):
        self._white_point = value
        self.program['u_whitePoint_2'] = value * value


    def show_ui(self):
        super().show_ui()
        self.white_point = imgui.slider_float(f'Threshold##{self.ui_index}', self.white_point, 0.0, 10.0, power=2.0)[1]