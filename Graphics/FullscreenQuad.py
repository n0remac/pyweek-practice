
import arcade
from array import array
#Class representing a mesh for a fullscreen quad with position and UV attributes
class FullscreenQuad():

    def __init__(self, context):

        #In the format of pos.x, pos.y uv.x, uv.y
        verticies = [
            -1.0, -1.0,     0.0, 0.0,
            -1.0, 1.0,      0.0, 1.0,
            1.0, -1.0,      1.0, 0.0,

            1.0, -1.0,      1.0, 0.0,
            -1.0, 1.0,      0.0, 1.0,
            1.0, 1.0,       1.0, 1.0
        ]

        self.buffer = context.buffer(data=array('f', verticies))
        self.buffer_description = arcade.gl.BufferDescription(self.buffer,
                                                        '2f 2f',
                                                        ['in_pos', 'in_uv'])
        self.fullscreen_quad_vao = context.geometry([self.buffer_description])

    #Render this geometry with the given OpenGL program
    def render(self, program):
        self.fullscreen_quad_vao.render(program)
        pass