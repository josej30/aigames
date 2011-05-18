from misc.vector3 import *

class SteeringOutput:
	linear = [0,-10,0]
	angular = 0.0

	def __init__(self,l=[0,0,0],a=0.0):
		self.linear = l
		self.angular = a

	def scale_steering(self,factor):
		self.linear = vectorTimes(self.linear,factor)
		self.angular *= factor
		return self

def sum_steering(s1,s2):

	steering = SteeringOutput()
	
	steering.linear = addition(s1.linear,s2.linear)
	steering.angular = s1.angular + s2.angular

	return steering
	
