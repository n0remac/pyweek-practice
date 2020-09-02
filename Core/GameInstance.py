import arcade
from typing import Optional

from Core.GameResources import GameResources
from Physics.PhysicsEngine import setup_physics_engine


class GameInstance:
	"""
	This is an instance of the game and all of the different components needed to render it.
	"""
	def __init__(self):

		# Core game resources
		self.game_resources = GameResources()

		# Physics engine
		self.physics_engine = setup_physics_engine(self.game_resources)

		# Set background color
		arcade.set_background_color(arcade.color.AMAZON)

	def on_key_press(self, key, modifiers):
		"""Called whenever a key is pressed. """
		pass

	def on_key_release(self, key, modifiers):
		"""Called when the user releases a key. """
		pass

	def on_mouse_motion(self, x, y, dx, dy):
		self.game_resources.on_mouse_motion(x, y, dx, dy)

	def on_draw(self):
		self.game_resources.on_draw()

	def on_draw_game(self):
		self.game_resources.on_draw_game()

	def on_update(self, delta_time):
		""" Movement and game logic """
		self.physics_engine.step()
		self.game_resources.on_update(delta_time)
