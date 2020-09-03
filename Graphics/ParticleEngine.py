from array import array
import arcade
import time
import random
from Graphics.RenderTarget import RenderTarget
from Graphics.FullscreenQuad import FullscreenQuad

#GPU based particle engine.
class ParticleEngine():
    
    def __init__(self, context):
        self.context = context
        self.start_time = time.time()
        self.mouse_pos = (0.0,0.0)
        self.mouse_power = 100.0
        #For testing purposes

        #Allocate vertex buffer

        #format is as follows

        #vec2 position
        #float radius
        #vec4 color

        tempParticleBuffer = [
            100.0, 100.0,   28.0, 32.0,     0.1,0.0,    1.0, 0.0, 0.0, 1.0,
            300.0, 100.0,   44.0, 48.0,     0.2,0.3,    0.0, 1.0, 0.0, 1.0,
            100.0, 300.0,   16.0, 64.0,     -0.1,0.0,    0.0, 0.0, 1.0, 1.0,
            300.0, 300.0,   64.0, 96.0,     0.0,0.0,    1.0, 1.0, 1.0, 1.0
        ]

        tempParticleBuffer = self.get_particles()
        asArray = array('f', tempParticleBuffer)

        self.bufferA = context.buffer(data=asArray)
        self.bufferB = context.buffer(data=asArray)

        self.buffer_description_a = arcade.gl.BufferDescription(self.bufferA,
                                                        '2f 2f 2f 4f',
                                                        ['in_pos', 'in_radius','in_vel', 'in_color'])

        self.buffer_description_b = arcade.gl.BufferDescription(self.bufferB,
                                                        '2f 2f 2f 4f',
                                                        ['in_pos', 'in_radius','in_vel', 'in_color'])

        self.particle_vao_a = context.geometry([self.buffer_description_a])
        self.particle_vao_b = context.geometry([self.buffer_description_b])

        #Compile shaders w/ geometry shader
        self.shader_program = context.load_program(
            vertex_shader='Graphics/Shaders/Particles/particle_test.vs',
            geometry_shader='Graphics/Shaders/Particles/particle_test.gs',
            fragment_shader='Graphics/Shaders/Particles/particle_test.fs'
        )

        self.physics_program = context.load_program(
            vertex_shader='Graphics/Shaders/Particles/particle_physics.vs',
        )

        self.emit_program = context.load_program(
            vertex_shader='Graphics/Shaders/Particles/particle_emit.vs',
        )

        self.emit_program['u_burst_power'] = (20.0,200.0)
        #user for rendering with point mode


        pass


    def get_particles(self):
        for i in range(1000000):
            yield 1920.0 / 2.0
            yield 1080.0 / 2.0

            yield 1.0
            yield 2.0

            yield 0.0
            yield 0.0

            yield 0.1
            yield 0.4
            yield 0.9
            yield 1.0



    def update(self):
        pass


    def flip_buffers(self):
        temp_buffer = self.bufferA
        temp_vao = self.particle_vao_a

        self.bufferA = self.bufferB
        self.particle_vao_a = self.particle_vao_b

        self.bufferB = temp_buffer
        self.particle_vao_b = temp_vao


    def test_burst(self, x, y):
        self.emit_program['u_burst_point'] = (x,y)
        self.particle_vao_a.transform(self.emit_program, self.bufferB)
        self.flip_buffers()
        self.mouse_power = 0.0



    def render(self, deltaT):

        self.mouse_power = min(100.0, self.mouse_power + 1)

        self.physics_program['u_delta_time'] = 0.016666
        self.physics_program['u_gravity'] = (0.0, -50.0)
        self.physics_program['u_drag'] = 0.998
        self.physics_program['u_mouse_pos'] = self.mouse_pos
        self.physics_program['u_mouse_power'] = self.mouse_power

        self.particle_vao_a.transform(self.physics_program, self.bufferB)


        #Flip Buffers
        self.flip_buffers()

        self.context.enable_only(self.context.BLEND)
        self.context.blend_func = self.context.BLEND_ADDITIVE

        self.shader_program['u_projection'] = self.context.projection_2d_matrix
        #if self.shader_program['u_time']:
        #    self.shader_program['u_time'] = time.time() - self.start_time

        self.particle_vao_a.render(self.shader_program, mode=self.context.POINTS)

        self.context.enable_only()

        #Emit new particles with geometry feedback

        #Update particles with geometry feedback

        #Set GL Additive

        #Draw particles to current target