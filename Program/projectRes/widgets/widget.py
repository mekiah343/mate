
class sphericalWidget:

	def __init__(self, position, size):
		
		self.position = {0, 0}
		self.destPosition = {0,0}

		self.tweenTime = 20
		self.transformSpeed = 1


		self.size = {0, 0}

		self.position = position
		self.size = size

	def update():
		self.position[1] = lerp(self.position[1], self.destPosition[1], (self.tweenTime * self.transformSpeed))
		self.position[2] = lerp(self.position[2], self.destPosition[2], (self.tweenTime * self.transformSpeed))

		translatePosition(self.position)


	def lerp(_value, _to, _smoothness):
		return _value + ((_to - _value) / _smoothness) 


	def setPosition(x, y):
		self.position = {x, y}

	def translatePosition(x, y):
		self.position[0] = self.position[0] + x
		self.position[1] = self.position[1] + y




