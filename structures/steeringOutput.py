class SteeringOutput:
	linear = [0,0,0]
	angular = 0.0

	def __init__(self,l=[0,0,0],a=0.0):
		self.linear = l
		self.angular = a
