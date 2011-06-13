from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pow, sqrt
from misc.vector3 import *
from physics.rules import inside_ob

class Bullet:

	
	maxSpeed = 100.0
	maxAcceleration = 100.0
	maxSpeedy = 100.0
	maxAccelerationy = 100.0
	position = [0,0,0]   # a 2 or 3D vector
	orientation = 0.0    # a single floating point value
	velocity = [10,10,10]   # another 2 or 3D vector
	radius = .5

	def __init__(self):
		self.radius = .5
	
	def update (self, steering,time):

		# Update the position and orientation
		
		self.position = vectorPlus(self.position,vectorTimes(self.velocity,time))
	

		if self.position[1] > 0:	
			steering.linear[1] = -30
			
		
		# And the velocity and the rotation
		self.velocity = vectorPlus(self.velocity,vectorTimes(steering.linear,time))
		self.orientation += steering.angular*time

		if self.position[1] <= 0 and self.velocity[1] <= 0:
			self.velocity[1] = 0

		# The velocity is along this direction, at full speed
		# If this is too fast, clip it to the max speed
		if vectorLengthnoy(self.velocity) > self.maxSpeed:
			self.velocity = normalize(self.velocity)
#			self.velocity[0] = self.velocity[0]*(self.maxSpeed/2)
#			self.velocity[2] = self.velocity[2]*(self.maxSpeed/2)
			self.velocity = vectorTimes(self.velocity,self.maxSpeed/2)
