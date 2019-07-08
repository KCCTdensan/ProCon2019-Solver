import numpy as np

class Agent:
	def __init__(self, position:[int, int]):
		self.__position = np.array(point)
		return

	def move(self, direction:[int, int]):
		self.__position += np.array(direction)
		return

	def getPosition(self):
		return self.__position