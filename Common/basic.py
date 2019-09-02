class Direction:
	def __init__(self, x, y):
		self.x = 0
		self.y = 0
		return

class Position:
	def __init__(self, x, y):
		self.x = 0
		self.y = 0
		return

	def move(self, direction:Direction):
		self.x += direction.x
		self.y += direction.y
		return

class Size:
	def __init__(self, width, height):
		self.width = 0
		self.height = 0
		return