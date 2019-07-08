from ..Engine.interface import Interface
import numpy as np
import random

class StageInfo:
	def __init__(self):
		return

	def __init__(self, boardPanels, boardX:int, boardY:int, numTurns:int):
		self.boardPanels = boardPanels
		self.boardX = boardX
		self.boardY = boardY
		self.numTurns = numTurns
		return

	def setRandom(self):
		self.boardX = random.randint(10, 20)
		self.boardY = random.randint(10, 20)
		return

class Stage:
	def __init__(self, stageInfo:StageInfo):
		self.__boardPanels = stageInfo.boardPanels
		self.__boardX = stageInfo.boardX
		self.__boardY = stageInfo.boardY
		self.__numTurns = stageInfo.numTurns
		self.__currentTurn = 0
		self.__redRegionScore = 0
		self.__redTileScore = 0
		self.__blueRegionScore = 0
		self.__blueTileScore = 0
		return

	def __updateScore(self):
		return

	def canAct(self, playerIntentions:list)->bool:
		return False

	def act(self, playerIntentions:list)->bool:
		if not canAct(playerIntentions):
			return False

		return True