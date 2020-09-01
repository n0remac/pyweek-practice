import arcade
from typing import Optional

from Physics.PhysicsEngine import setup_physics_engine


class GameInstanceDependencies:
	def __init__(self):
		self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

	def setup(self):
		self.physics_engine = setup_physics_engine(self)
