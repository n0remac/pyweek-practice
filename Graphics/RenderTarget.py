
import arcade

class RenderTarget():

    def __init__(self,context, width, height): #TODO: Optional format settings
        if width <= 0:
            raise ValueError("width must be greater than zero")
        if height <= 0:
            raise ValueError("height must be greater than zero")

        #Allocate framebuffer texture
        self.framebuffer_target_texture = context.texture(
            (width,height),
            components=4,
            dtype='f1')

        #Create a framebuffer object with that texture to render to
        self.framebuffer = context.framebuffer(color_attachments=[self.framebuffer_target_texture])

        #Prevents rendering bugs later. Don't know enought about arcade to know why
        self.framebuffer.use()
        self.framebuffer.clear()

        self.width = width
        self.height = height

        self.is_valid = True

    def release(self):
        #Relesase OpenGL resources if they already exist
        if self.framebuffer_target_texture is not None:
            self.framebuffer_target_texture.release()
            self.framebuffer_target_texture = None
        if self.framebuffer is not None:
            self.framebuffer.release()
            self.framebuffer = None

        is_valid = False

    def get_is_valid(self):
        return self.is_valid

    def bind_as_texture(self, texture_slot):
        if not self.is_valid:
            raise RuntimeError("This RenderTarget is not valid, check get_is_valid before using")
        if texture_slot < 0:
            raise ValueError("texture_slot must be zero or greater")
        self.framebuffer_target_texture.use(texture_slot)

    #Bind as a framebuffer (all drawing will now be done to this target)
    #Note: by default, this method will also set the current viewport to be the full render target
    def bind_as_framebuffer(self, set_viewport=True):
        if not self.is_valid:
            raise RuntimeError("This RenderTarget is not valid, check get_is_valid before using")
        self.framebuffer.use()
        if set_viewport:
            arcade.set_viewport(0,self.width, 0, self.height)

    #Clears the framebuffer to a given color, in normalized 0-1 values
    def clear(self, color):
        self.framebuffer.clear(color, normalized=True)