import numpy as np
import random

from ..Common.field import Field
from field import Field

class StageInfo:
	def __init__(self, field:Field, numTurns:int):
		self.field = field
		self.numTurns = numTurns
		return

	def setRandom(self):
		self.boardX = random.randint(10, 20)
		self.boardY = random.randint(10, 20)
		return

class Score:
	def __init__(self):
		pass

	def __updateTileScore(self, field:Field):
		pass

	def __updateRegionScore(self, field:Field):
		pass

	def update(self, boardPanels):
		self.__updateTileScore(boardPanels)
		self.__updateRegionScore(boardPanels)

class Stage:
	def __init__(self, stageInfo:StageInfo):
		self.__field = stageInfo.field
		self.__numTurns = stageInfo.numTurns
		self.__currentTurn = 0
		self.__scoreRed = Score()
		self.__scoreBlue = Score()
		return

	def __updateScore(self):
		self.__scoreRed.update(self.__field)
		self.__scoreBlue.update(self.__field)
		return

	def canAct(self, playerIntentions:list)->bool:
		return False

	def act(self, playerIntentions)->bool:
		if not canAct(playerIntentions):
			return False
		self.__updateScore()
		return True