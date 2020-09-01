
import math
import arcade
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad

#Basic Split tone shader with the following arguments:

#threshold-> (Default 0.5) The middle point between shadows and highlights 0.0->1.0 for LDR, 0.0->A LOT(brightest light in scene) for HDR
#Crossover-> (Defualt 0.05) The sizeof the band where the 2 colors are blended between, this value indicates the total length in brightness for this band. 
#shadow_color-> (Default (0.0,0.0,0.0)) The color to add to shadows (or subtract if this is negative)
#highlight_color-> (Default (0.0,0.0,0.0)) The color to add to highlights (or subtract if this is negative)
#NOTE: Values can be HDR if this stage runs before tonemapping
class SplitTone(PostProcessingStage):

    def __init__(self, context):
        super().__init__()
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/SplitTone.fs'
        )
        self.program['t_source'] = 0

        self.threshold = 0.5
        self.crossover = 0.05
        self.shadow_color = (0.0,0.0,0.0)
        self.highlight_color = (0.0,0.0,0.0)

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self,value):
        self._threshold = value
        self.program['u_threshold'] = value

    @property
    def crossover(self):
        return self._crossover

    @crossover.setter
    def crossover(self,value):
        value = max(0.0, value)
        self._crossover = value
        self.program['u_crossover_half'] = value * 0.5

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