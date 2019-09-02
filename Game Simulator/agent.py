import numpy as np

from ..Common.basic import Position
from ..Common.basic import Direction

class Agent:
	def __init__(self, position:Position):
		self.__position = position
		return

	def move(self, direction:Direction):
		self.__position.move(direction)
		return

	def getPosition(self)->Position:
		return self.__position