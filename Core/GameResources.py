from typing import Optional

import arcade

from Constants.Game import SPRITE_SCALING_TILES, SPRITE_SCALING_PLAYER, SPRITE_SIZE


class GameResources:
	"""
	In theory, this should be the place where you load in resources that the game uses via Arcade's various APIs.
	Currently a grab bag of Arcade resources that get stored, updated, and rendered.
	Unfortunately Arcade doesn't support an immutable API for stuff (probably for simplicity), so have to live with
	mutating the locations of sprite instances to move them around. Oh well!
	"""

	def __init__(self):

		self.hello = arcade.Sprite("Graphics/hello_world.png")
		self.hello.scale = 0.25

		self.sprite_list = arcade.SpriteList()

		# Create the sprite lists
		self.player_list = arcade.SpriteList()
		self.bullet_list = arcade.SpriteList()

		# Read in the tiled map
		map_name = "arcade-resources/tmx_maps/map.tmx"
		my_map = arcade.tilemap.read_tmx(map_name)
		self.wall_list = arcade.tilemap.process_layer(
			my_map, "Platforms", SPRITE_SCALING_TILES
		)
		self.item_list = arcade.tilemap.process_layer(
			my_map, "Dynamic Items", SPRITE_SCALING_TILES
		)

		# Create player sprite
		self.player_sprite = arcade.Sprite(
			"arcade-resources/images/animated_characters/female_person/femalePerson_idle.png",
			SPRITE_SCALING_PLAYER,
		)

		# Set player location
		grid_x = 1
		grid_y = 1
		self.player_sprite.center_x = SPRITE_SIZE * grid_x + SPRITE_SIZE / 2
		self.player_sprite.center_y = SPRITE_SIZE * grid_y + SPRITE_SIZE / 2
		# Add to player sprite list
		self.player_list.append(self.player_sprite)

		self.sprite_list.append(self.hello)

	def on_mouse_motion(self, x, y, dx, dy):
		self.hello.center_x = x
		self.hello.center_y = y

	def on_draw(self):
		self.wall_list.draw()
		self.bullet_list.draw()
		self.item_list.draw()
		self.player_list.draw()

	def on_draw_game(self):
		self.sprite_list.draw()

	def on_update(self, delta_time):
		pass
