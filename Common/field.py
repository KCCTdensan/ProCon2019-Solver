import numpy as np

from .basic import Size
from .basic import Position
from .panel import Panel

class Field:
	def __init__(self, size:Size, panels:np.array = None):
		self.__size = size
		self.__panels = []
		return

	def getSize(self)->Size:
		return self.__size

	def getPanel(self, position:Position)->Panel:
		return self.__panels[position.y][position.x]