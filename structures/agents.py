from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pow, sqrt
from misc.vector3 import *

class Agent:

	maxSpeed = 12
	maxAcceleration = 15
	radius = 0
	position = [0,0,0]   # a 2 or 3D vector
	orientation = 0.0    # a single floating point value
	velocity = [0,0,0]   # another 2 or 3D vector
	rotation = 0.0       # a single floating point value

	def __init__(self):
		self.radius = 1
	
	def update (self, steering, time):

		# Update the position and orientation
		self.position = vectorPlus(self.position,vectorTimes(self.velocity,time))
		self.orientation += self.rotation*time

		# Negative position check
		if self.position[1] < 0.0 :
			self.position[1] = 0.0

		if self.position[1] > 0 :		
			steering.linear[1] = -2.0
			#steering.linear = [0,-2.0,0]
		
		# And the velocity and the rotation
		self.velocity = vectorPlus(self.velocity,vectorTimes(steering.linear,time))
		self.orientation += steering.angular*time

		# Negative position check
		if self.position[1] <= 0 and self.velocity[1] < 0 :
			self.velocity[1] = 0

		# The velocity is along this direction, at full speed
		# If this is too fast, clip it to the max speed
		if vectorLength(self.velocity) > self.maxSpeed:
			self.velocity = normalize(self.velocity)
			self.velocity = vectorTimes(self.velocity,self.maxSpeed)
