
import arcade
import imgui
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad

class Vignette(PostProcessingStage):

    def __init__(self, context):
        super().__init__()
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/vignette.fs'
        )
        self.program['t_source'] = 0

        self.start_distance = 0.8
        self.end_distance = 1.5
        self.strength = 1.0
        self.scale = (1.0, 1.0)
        self.color = (0.0,0.0,0.0)

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)
        self.quad.render(self.program)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self,value):
        self._strength = value
        self.program['u_strength'] = value


    @property
    def start_distance(self):
        return self._start_distance

    @start_distance.setter
    def start_distance(self,value):
        self._start_distance = value
        self.program['u_start_distance'] = value

    @property
    def end_distance(self):
        return self._end_distance

    @end_distance.setter
    def end_distance(self,value):
        self._end_distance = value
        self.program['u_end_distance'] = value

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self,value):
        self._scale = value
        self.program['u_scale'] = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color =value
        self.program['u_color'] = value

    def show_ui(self):
        super().show_ui()

        self.start_distance = imgui.slider_float(f'Start Distance##{self.ui_index}', self.start_distance, -1.0, 3.0)[1]
        self.end_distance = imgui.slider_float(f'End Distance##{self.ui_index}', self.end_distance, -1.0, 3.0)[1]
        self.strength = imgui.slider_float(f'Strength##{self.ui_index}', self.strength, 0.0, 2.0)[1]
        self.scale = imgui.slider_float2(f'Scale##{self.ui_index}', self._scale[0], self._scale[1], 0.0,4.0)[1]

        self.color = imgui.color_edit3(f'Color##{self.ui_index}', *self.color)[1]
