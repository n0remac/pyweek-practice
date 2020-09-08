
import arcade
import imgui
from array import array
from PIL import Image
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad

class ColorGrading(PostProcessingStage):

    def __init__(self, context):
        super().__init__()
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/color_grading.fs'
        )
        self.program['t_source'] = 0
        self.strength = 1.0
        #TODO: Load Texture

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)

        self.quad.render(self.program)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value
        self.program['u_strength'] = value




    #Write a copy of the default color LUT to disk
    def write_default_lut(self,  path):
        
        def value_for_pos(pos):
            return pos * 17

        cols = 16 * 16
        rows = 16

        data = [0 for x in range(cols*rows*4)]

        for b in range(16):
            for g in range(16):
                for r in range(16):
                    #compute address
                    x = r + 16 * b
                    y = g

                    addresss_base = 4 * (x + y * cols)
                    data[addresss_base] = value_for_pos(r)
                    data[addresss_base+1] = value_for_pos(g)
                    data[addresss_base+2] = value_for_pos(b)
                    data[addresss_base+3] = 255


        byteBuffer = bytes(data)

        lut = Image.frombytes('RGBA', (cols,rows), byteBuffer)
        lut.save('./lut.png')
        pass