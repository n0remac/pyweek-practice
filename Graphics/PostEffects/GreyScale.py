
import math
import arcade
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad
import imgui
import imgui.core


class GreyScale(PostProcessingStage):

    def __init__(self, context):
        super().__init__()
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/GreyScale.fs'
        )
        self.program['t_source'] = 0

        self.strength = 1.0
        self.shadow_color = (0.0,0.0,0.0)
        self.highlight_color = (1.0,1.0,1.0)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self,value):
        self._strength = value
        self.program['u_strength'] = value

    @property
    def shadow_color(self):
        return self._shadow_color

    @shadow_color.setter
    def shadow_color(self,value):
        self._shadow_color = value
        self.program['u_shadow_color'] = value

    @property
    def highlight_color(self):
        return self._highlight_color

    @highlight_color.setter
    def highlight_color(self, value):
        self._highlight_color = value
        self.program['u_highlight_color'] = value

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)

        self.quad.render(self.program)

    def show_ui(self):
        super().show_ui()
        self.strength = imgui.slider_float(f'Strength##{self.ui_index}', self.strength, 0.0, 1.0)[1]
        self.shadow_color = imgui.color_edit3(f'Shadow Color##{self.ui_index}', *self.shadow_color)[1]
        self.highlight_color = imgui.color_edit3(f'Highlight Color##{self.ui_index}', *self.highlight_color)[1]
       