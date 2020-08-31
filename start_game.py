import arcade
from Graphics import RenderingPipeline
from Graphics import PostProcessingChain
from Graphics.PostEffects.InvertColors import InvertColors
from Graphics.PostEffects.TrashChromaticAberration import TrashChromaticAberration

SCREEN_TITLE = "PyMunk Platformer"

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_TILES = 0.5

# Scaled sprite size for tiles
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

# Size of grid to show on screen, in number of tiles
SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

# Size of screen to show, in pixels
SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)

        # Player sprite
        self.player_sprite: Optional[arcade.Sprite] = None

        # Sprite lists we need
        self.player_list: Optional[arcade.SpriteList] = None
        self.wall_list: Optional[arcade.SpriteList] = None
        self.bullet_list: Optional[arcade.SpriteList] = None
        self.item_list: Optional[arcade.SpriteList] = None

        # Track the current state of what key is pressed
        self.left_pressed: bool = False
        self.right_pressed: bool = False

        # Set background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up everything with the game """

        windowSize = self.get_size()

        self.render_pipeline = RenderingPipeline.RenderingPipeline(
            self, windowSize[0], windowSize[1]
        )
        self.render_pipeline.on_draw_frame = self.on_draw_game
        self.render_pipeline.background_color = (0.1, 0.1, 0.1, 1.0)

        self.post_process = PostProcessingChain.PostProcessingChain(
            self.ctx, windowSize[0], windowSize[1]
        )
        self.render_pipeline.post_processing_chain = self.post_process

        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))
        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))
        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))
        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))

        self.hello = arcade.Sprite("Graphics/hello_world.png")
        self.spriteList = arcade.SpriteList()
        self.spriteList.append(self.hello)
        self.hello.scale = 0.25
        pass

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
        self.spriteList.draw()
        pass


def main():
    """ Main method """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
