import numpy as np

from ..Common.basic import Position
from ..Common.basic import Direction

class Agent:
	def __init__(self, field:Field, position:Position):
		self.__field = field
		self.__position = position
		return

	def getPosition(self)->Position:
		return self.__position

	def canMove(direction:Direction)->bool:
		nextPosition = self.__position.copy()
		nextPosition.move(direction)
		return (nextPosition.x >= 0) and (nextPosition.x < self.__field.getSize().x) and (nextPosition.y >= 0) and (nextPosition.y < self.__field.getSize().y)
	
	def move(self, direction:Direction):
		self.__position.move(direction)
		return