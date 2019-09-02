import numpy as np

from .basic import Size
from .basic import Position

class Field:
	def __init__(self, size:Size, panels:np.array = None):
		self.__size = size
		self.__panels = []
		return

	def getSize(self)->Size:
		return self.__size

	def getPanel(self, position:Position)->int:
		return self.__panels[position.y][position.x]

	def setPanel(self, position:Position, state:int):
		self.__panels[position.y][position.x] = state
		return

	def getAllPanels(self)->tuple:
		return tuple(self.__panels)