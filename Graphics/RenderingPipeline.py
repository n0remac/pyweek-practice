import arcade
from .FullscreenQuad import FullscreenQuad

class RenderingPipeline():

    def resize_render_pipeline(self, width, height):

        if width <= 0:
            raise ValueError("width must be greater than zero")
        if height <= 0:
            raise ValueError("height must be greater than zero")

        #Relesase OpenGL resources if they already exist
        if self.framebuffer_target_texture is not None:
            self.framebuffer_target_texture.release()
            self.framebuffer_target_texture = None
        if self.framebuffer is not None:
            self.framebuffer.release()
            self.framebuffer = None

        #Allocate framebuffer texture
        self.framebuffer_target_texture = self.context.texture(
            (width,height),
            components=4,
            dtype='f1')

        #Create a framebuffer object with that texture to render to
        self.framebuffer = self.context.framebuffer(color_attachments=[self.framebuffer_target_texture])

        #Prevents rendering bugs later. Don't know enought about arcade to know why
        self.framebuffer.use()
        self.framebuffer.clear()

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

        self.framebuffer_target_texture = None
        self.framebuffer = None

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
        self.framebuffer.use()
        arcade.set_viewport(0,self.render_width, 0, self.render_height)

        #Clear screen before render
        self.framebuffer.clear(self.background_color, normalized=True)


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

        self.framebuffer_target_texture.use(0)
        self.fullscreen_quad.render(self.blit_program)

        #draw post-post processing elements
        if self.on_draw_after_post_processing is not None:
            self.on_draw_after_post_processing()

        if self.on_post_render is not None:
            self.on_post_render() 