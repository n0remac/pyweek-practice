"""
Example of Pymunk Physics Engine Platformer
"""
import arcade
from Graphics import RenderingPipeline
from Graphics import PostProcessingChain
from Graphics.TestLightingController import TestLightingController

from Graphics.PostEffects.InvertColors import InvertColors
from Graphics.PostEffects.TrashChromaticAberration import TrashChromaticAberration
from Graphics.PostEffects.Bloom import Bloom
from Graphics.PostEffects.Tonemap import Tonemap
from Graphics.PostEffects.SplitTone import SplitTone
from Graphics.PostEffects.Vignette import Vignette
from Graphics.PostEffects.GoodChromaticAberration import GoodChromaticAberration
from Graphics.PostEffects.ColorGrading import ColorGrading

from arcade_imgui.arcadeimgui.integrations.arcade_renderer import ArcadeRenderer
import pyglet
import imgui
import imgui.core

SCREEN_TITLE = "PyMunk Platformer"

# Size of screen to show, in pixels
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)
        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

    def setup(self):
        """ Set up everything with the game """


        windowSize = self.get_size()

        self.render_pipeline = RenderingPipeline.RenderingPipeline(self, windowSize[0], windowSize[1])
        self.render_pipeline.on_draw_frame = self.on_draw_game
        self.render_pipeline.background_color = (0.1,0.1,0.1,1.0)

        self.post_process = PostProcessingChain.PostProcessingChain(self.ctx, windowSize[0], windowSize[1])
        self.render_pipeline.post_processing_chain = self.post_process

        #Create lighting controller
        self.lighting = TestLightingController(self.ctx)
        self.lighting.ambient_light = (0.1,0.1,0.1,1.0)

        #add other nonsense because why not
        #self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))

        #add some bloom
        self.bloom = Bloom(self.ctx, 15, 3.0, 2.0, 1.0)

        #Add a tonemap stage after the bloom

        #Add a split tone stage after the bloom
        self.split_tone = SplitTone(self.ctx)
        self.split_tone.threshold = 0.75
        self.split_tone.crossover = 0.05
        self.split_tone.shadow_color = (0.0, 0.1, 0.0)
        self.split_tone.highlight_color = (0.0, 0.0, 0.1)

        self.vignette = Vignette(self.ctx)

        self.hello = arcade.Sprite('Graphics/hello_world.png')
        self.spriteList = arcade.SpriteList()
        self.spriteList.append(self.hello)
        self.hello.scale = 0.25

        self.bricks = arcade.SpriteList()

        for x in range(4):
            for y in range(4):
                sprite = arcade.Sprite('Graphics/temp_bricks.jpg')
                sprite.center_x = 0.1 * x * sprite.width
                sprite.center_y = 0.1 * y * sprite.height
                sprite.scale = 0.1
                self.bricks.append(sprite)

        


        self.lightA = self.lighting.create_point_light((200,200),128, (3.0,3.0,3.0,3.0) )

        self.lighting.create_point_light((150,150),196, (2.0,0.0,0.0,1.0) )
        self.lighting.create_point_light((275,300),196, (0.0,2.0,0.0,1.0) )
        self.lighting.create_point_light((400,150),196, (0.0,0.0,2.0,1.0) )


        self.show_postprocess_ui = True
        self.show_imgui_test = False

        self.goodAberr = GoodChromaticAberration(self.ctx)

        self.color_grading = ColorGrading(self.ctx)
        
        self.cgt = arcade.load_texture("./lut_cold.png")
        self.color_grading.set_texture(self.cgt)


        #Build post-process chain in one spot for easier toggeling

        #Make sure to add the lighting post processing as the first stage
        #self.post_process.add_stage(self.lighting.get_apply_light_stage())

        #self.post_process.add_stage(self.bloom)
        #self.post_process.add_stage(Tonemap(self.ctx, 1.5))
        #self.post_process.add_stage(self.split_tone)
        #self.post_process.add_stage(self.vignette)
        self.post_process.add_stage(self.goodAberr)

        self.post_process.add_stage(self.color_grading)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.P:
            self.show_postprocess_ui = not self.show_postprocess_ui

        if key == arcade.key.I:
            self.show_imgui_test = not self.show_imgui_test

        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.hello.center_x = x
        self.hello.center_y = y

        self.lightA.position = (x,y)

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass

    def on_draw(self):
        """ Draw everything """

        self.lighting.draw_light_buffer(self.ctx, self.width, self.height)
        #self.render_pipeline.debug_rt = self.lighting.light_buffer

        self.render_pipeline.draw_frame()

        self.on_draw_gui()

    def on_draw_game(self):
        self.bricks.draw()
        self.spriteList.draw()
        pass

    def on_draw_gui(self):
        imgui.new_frame()

        if self.show_imgui_test:
            imgui.show_test_window()
        if self.show_postprocess_ui:
            self.post_process.show_postprocess_ui()

        imgui.end_frame()
        imgui.render()       
        self.renderer.render(imgui.get_draw_data())

def main():
    """ Main method """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()