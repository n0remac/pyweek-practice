
import arcade
import imgui
from array import array
from PIL import Image
from Graphics.PostProcessingChain import PostProcessingStage
from Graphics.FullscreenQuad import FullscreenQuad

class ColorGrading(PostProcessingStage):

    def __init__(self, context):
        super().__init__()
        self.context = context
        self.quad = FullscreenQuad(context)
        self.program = context.load_program(
            vertex_shader='Graphics/Shaders/fullscreen_quad.vs',
            fragment_shader='Graphics/Shaders/color_grading.fs'
        )
        self.program['t_source'] = 0
        self.program['t_lut'] = 1

        self.strength = 1.0
        #TODO: Load Texture

        byte_buffer = self.generate_default_lut()
        self.set_texture_from_bytes(byte_buffer)

    def apply(self, source, target, width, height):
        
        target.bind_as_framebuffer()
        source.bind_as_texture(0)
        self.lut_texture.use(1)
        self.quad.render(self.program)

    def set_texture(self, texture):
        byte_array = texture.image.tobytes()
        self.set_texture_from_bytes(byte_array)

    def set_texture_from_bytes(self,bytes):    
        self.lut_texture = self.context.texture(
            (256,16),
            components=4,
            dtype='f1',
            data=bytes,
            wrap_x=self.context.CLAMP_TO_EDGE,
            wrap_y=self.context.CLAMP_TO_EDGE,
            filter=(self.context.NEAREST,self.context.NEAREST)
        )

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value
        self.program['u_strength'] = value

    def show_ui(self):
        super().show_ui()
        self.strength = imgui.slider_float(f'Strength##{self.ui_index}', self.strength, 0.0, 1.0)[1]

    def generate_default_lut(self):
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
        return byteBuffer

    #Write a copy of the default color LUT to disk
    def write_default_lut(self,  path):
        
        byteBuffer = self.generate_default_lut()

        lut = Image.frombytes('RGBA', (cols,rows), byteBuffer)
        lut.save('./lut.png')
        pass

