"""
Example of Pymunk Physics Engine Platformer
"""
import arcade
from Graphics import RenderingPipeline
from Graphics import PostProcessingChain
from Graphics.PostEffects.InvertColors import InvertColors
from Graphics.PostEffects.TrashChromaticAberration import TrashChromaticAberration

SCREEN_TITLE = "PyMunk Platformer"

# Size of screen to show, in pixels
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)


    def setup(self):
        """ Set up everything with the game """

        windowSize = self.get_size()

        self.render_pipeline = RenderingPipeline.RenderingPipeline(self, windowSize[0], windowSize[1])
        self.render_pipeline.on_draw_frame = self.on_draw_game
        self.render_pipeline.background_color = (0.1,0.1,0.1,1.0)

        self.post_process = PostProcessingChain.PostProcessingChain(self.ctx, windowSize[0], windowSize[1])
        self.render_pipeline.post_processing_chain = self.post_process

        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))

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

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.hello.center_x = x
        self.hello.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass

    def on_draw(self):
        """ Draw everything """
        self.render_pipeline.draw_frame()

    def on_draw_game(self):
        self.bricks.draw()
        self.spriteList.draw()
        pass

def main():
    """ Main method """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()