class Panel:
	def __init__(self, point:int):
		self.__point = point
		self.__tile = None
		self.__isRegionOfRed = False
		self.__isRegionOfBlue = False
		return

	def putRedTile(self):
		self.__tile = 'r'
		self.__isRegionOfRed = False
		return

	def putBlueTile(self):
		self.__tile = 'b'
		self.__isRegionOfBlue = False
		return

	def removeTile(self):
		self.__tile = None
		return

	def getPoint(self)->int:
		return self.__point

	def isRedTile(self)->bool:
		return self.__tile == 'r'

	def isBlueTile(self)->bool:
		return self.__tile == 'b'

	def validateRegionOfRed(self):
		self.__isRegionOfRed = True
		if self.__tile == 'r':
			self.__tile = None
		return

	def invalidateRegionOfRed(self):
		self.__isRegionOfRed = False
		return

	def invalidateRegionOfBlue(self):
		self.__isRegionOfBlue = False
		return

	def validateRegionOfBlue(self):
		self.__isRegionOfBlue = True
		if self.__tile == 'b':
			self.__tile = None
		return

	def isRegionOfRed(self)->bool:
		return self.__isRegionOfRed

	def isRegionOfBlue(self)->bool:
		return self.__isRegionOfBlue