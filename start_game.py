import arcade
from typing import Optional

from Constants.Game import SPRITE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Core.GameInstance import GameInstance
from Core.GameResources import GameResources
from Graphics import RenderingPipeline
from Graphics import PostProcessingChain
from Graphics.PostEffects.InvertColors import InvertColors
from Graphics.PostEffects.TrashChromaticAberration import TrashChromaticAberration


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)

        self.game_instance: Optional[GameInstance] = None

        # Track the current state of what key is pressed
        # TODO: Figure out where we want to store state variables.
        self.left_pressed: bool = False
        self.right_pressed: bool = False

        # Render Pipeline
        self.render_pipeline = Optional[RenderingPipeline.RenderingPipeline]
        self.post_process = Optional[PostProcessingChain.PostProcessingChain]

    def setup(self):
        """ Set up everything with the game """

        window_size = self.get_size()

        self.game_instance = GameInstance()

        # TODO: Move this into the GameInstance.
        self.render_pipeline = RenderingPipeline.RenderingPipeline(
            self, window_size[0], window_size[1]
        )
        self.render_pipeline.on_draw_frame = self.on_draw_game
        self.render_pipeline.background_color = (0.1, 0.1, 0.1, 1.0)

        self.post_process = PostProcessingChain.PostProcessingChain(
            self.ctx, window_size[0], window_size[1]
        )
        self.render_pipeline.post_processing_chain = self.post_process

        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))
        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))
        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))
        self.post_process.add_stage(TrashChromaticAberration(self.ctx, 0.005))

        # Sprites can be added to to the spriteList to be put through the post processor
        """
        for w in self.wall_list:
            self.spriteList.append(w)
        """

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.game_instance.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        self.game_instance.on_key_release(key, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.game_instance.on_mouse_motion(x, y, dx, dy)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.game_instance.on_update(delta_time)

    def on_draw(self):
        """ Draw everything """
        self.render_pipeline.draw_frame()
        self.game_instance.on_draw()

    def on_draw_game(self):
        self.game_instance.on_draw_game()


def main():
    """ Main method """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
