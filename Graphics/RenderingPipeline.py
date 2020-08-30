import arcade
from .FullscreenQuad import FullscreenQuad
from .RenderTarget import RenderTarget

class RenderingPipeline():

    def resize_render_pipeline(self, width, height):

        if width <= 0:
            raise ValueError("width must be greater than zero")
        if height <= 0:
            raise ValueError("height must be greater than zero")

        #$Release previous render target if allocated
        if self.render_target is not None:
            self.render_target.release()
            self.render_target = None

        self.render_target = RenderTarget(self.context, width, height)

        self.render_width = width
        self.render_height = height

        #TODO: Resise post processing chain
        if self.post_processing_chain is not None:
            pass

        pass


    def __init__(self, window, width, height):

        if window is None:
            raise TypeError("Window cannot be null")

        self.main_window = window
        self.context = window.ctx


        self.on_pre_render = None
        self.on_post_render = None
        self.on_draw_frame = None
        self.on_draw_after_post_processing = None

        self.post_processing_chain = None
        self.post_processing_enabled = False

        self.render_target = None

        self.background_color = (0.5,0.5,0.5,1.0)

        self.resize_render_pipeline(width, height)

        self.fullscreen_quad = FullscreenQuad(self.context)
        self.blit_program = self.__load_blit_program()

    #Create a OpenGL program to blit one framebuffer onto another
    def __load_blit_program(self):

        blit_program = self.context.load_program(
            vertex_shader="Graphics/Shaders/fullscreen_quad.vs",
            fragment_shader="Graphics/Shaders/fullscreen_blit.fs"
        )
        blit_program['srcTexture'] = 0
        return blit_program

    def draw_frame(self):

        arcade.start_render()
        if self.on_pre_render is not None:
            self.on_pre_render()

        #Set target framebuffer & viewport
        self.render_target.bind_as_framebuffer()

        #Clear screen before render
        self.render_target.clear(self.background_color)

        #Execute primary drawing callback
        if self.on_draw_frame is not None:
            self.on_draw_frame()
        else:
            pass

        #execute post-processing chain

        #blit final result of post-processing to the main viewport
        self.main_window.use()
        arcade.set_viewport(0,self.render_width, 0, self.render_height)
        self.main_window.clear()

        self.render_target.bind_as_texture(0)
        self.fullscreen_quad.render(self.blit_program)

        #draw post-post processing elements
        if self.on_draw_after_post_processing is not None:
            self.on_draw_after_post_processing()

        if self.on_post_render is not None:
            self.on_post_render() 