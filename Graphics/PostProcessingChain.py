import arcade
from Graphics.RenderTarget import RenderTarget
import imgui
import imgui.core

class PostProcessingChain():

    #Create a new post processing chain from a opengl context, and screen widht+height
    def __init__(self, context, width, height):

        self.chain = []
        self.context = context

        self.rt_ping = None #Read from this
        self.rt_pong = None #And write to this

        self.resize_chain(width,height)

    #Resize all the internal render targets of the post processing chain
    def resize_chain(self, width, height):

        if self.rt_ping is not None:
            self.rt_ping.release()
        if self.rt_pong is not None:
            self.rt_pong.release()
        
        self.rt_ping = RenderTarget(self.context, width, height, 'f2')
        self.rt_pong = RenderTarget(self.context, width, height, 'f2')

        self.width = width
        self.height = height
            

    def add_stage(self, stage):
        if not isinstance(stage, PostProcessingStage):
            raise TypeError("stage must derrive from PostProcessingStage")

        if stage in self.chain:
            return
        self.chain.append(stage)
    

    def remove_stage(self, stage):
        self.chain.remove(stage)


    #Apply the post processing chain to a source render target, return a reference to the
    #texture containing the fully processed final image
    def apply_chain(self, source):



        #handle the special case of no stages
        if len(self.chain) == 0:
            return source

        #handle the special case of the first chain stage tha reads directly from the 
        #input texture instead of the ping buffer
        self.__apply_stage(self.chain[0], source, self.rt_pong)

        #Skip first element in chain as it was applied above
        for x in self.chain[1:]:
            self.__apply_stage(x, self.rt_ping, self.rt_pong)

        #All writes go to rt_pong, but we flip the buffers after applying a stage
        #So rt_ping ends up with the final iamge
        return self.rt_ping
     

    def __apply_stage(self, stage, source, target):

        #Apply stage
        stage.apply(source,target, self.width, self.height)

        #Swap buffers
        temp = self.rt_pong
        self.rt_pong = self.rt_ping
        self.rt_ping = temp
        pass

    def show_postprocess_ui(self):
        imgui.begin("Post-Processing window", False)
        imgui.text("Post-Processing Stages:")
        imgui.separator()
        for stage in self.chain:
            if imgui.collapsing_header(type(stage).__name__, flags=imgui.TREE_NODE_DEFAULT_OPEN)[0]:
                imgui.text('asdf')
                #imgui.end()

        imgui.end()


class PostProcessingStage():
    def __init__(self):
        pass

    def apply(self, source, target, width, height):
        raise NotImplementedError("This method must be implemente by a derrived class")

    def show_ui(self):
        pass