from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pow, sqrt
from misc.vector3 import *
from physics.rules import inside_ob
from bullets import *

class Agent:

	maxSpeed = 12.0
	maxAcceleration = 15.0
	maxSpeedy = 10.0
	maxAccelerationy = 15.0
	radius = 0
	position = [0,0,0]   # a 2 or 3D vector
	orientation = 0.0    # a single floating point value
	velocity = [0,0,0]   # another 2 or 3D vector
	rotation = 0.0       # a single floating point value
	life = 20            # Agent's life
	maxlife = 20         # Agent's max life
	state = "Wander"     # Agent's behavior
	bullets = []

	def __init__(self):
		self.radius = 1
	
	def update (self, steering, time, obs, flag):

		# Update the position and orientation
		
		self.position = vectorPlus(self.position,vectorTimes(self.velocity,time))
		self.orientation += self.rotation*time

		# Negative position check
		if self.position[1] < 0.0 :
			self.position[1] = 0.0

		# We have to check wether or not
		# the agent is inside (over) and obstacle. If so (or the
		# agent is on the floor) we do not use the gravity
		grav = True
		for ob in obs:
			if inside_ob(self,ob):
				self.position[1] = ob.height
				grav = False

		if self.position[1] > 0 and flag == "auto":		
			steering.linear[1] = -self.maxAccelerationy
			
		if not grav:
			steering.linear[1] = 0
			self.velocity[1] = 0
		
		# And the velocity and the rotation
		self.velocity = vectorPlus(self.velocity,vectorTimes(steering.linear,time))
		self.orientation += steering.angular*time

		if self.position[1] <= 0 and self.velocity[1] <= 0:
			self.velocity[1] = 0

		# The velocity is along this direction, at full speed
		# If this is too fast, clip it to the max speed
		if vectorLengthnoy(self.velocity) > self.maxSpeed:
			self.velocity = normalize1(self.velocity)
#			self.velocity[0] = self.velocity[0]*(self.maxSpeed/2)
#			self.velocity[2] = self.velocity[2]*(self.maxSpeed/2)
			self.velocity = vectorTimes1(self.velocity,self.maxSpeed/2)

def agentNear(agent,chars,distance):
	for char in chars:
		if agent.position != char.position:
			if near(agent,char,distance):
				return char
	return None

def near(agent,target,distance):
	if sqrt((pow((agent.position[2]-target.position[2]),2.0)) +
		(pow((agent.position[0]-target.position[0]),2.0)) ) < distance:
			return True
