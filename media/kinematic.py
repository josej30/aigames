from agents import *
from kinematicSteeringOutput import *
from kinematicWander import *
from math import pow , sqrt, atan2, sin, cos
from random import random
from steeringOutput import *


maxSpeed = 15
maxAcceleration = 5

def getNewOrientation(currentOrientation, velocity):

	# Make sure we have a velocity
	if velocity != [0,0,0]:

	# Calculate orientation using an arc tangent of
 	# the velocity components.
 		return atan2(-velocity[0],velocity[2])
 	# Otherwise use the current orientation

   	else:
   		return currentOrientation


def normalize(vector):
	factor = sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))
	if factor != 0:
		return [vector[0]/factor,vector[1]/factor,vector[2]/factor]
	else:
		return vector
	
def distanceToRadius(agent,target):
	return sqrt(pow(target.position[0]-agent.position[0],2) + pow(target.position[2]-agent.position[2],2))

def vectorTimes(v,x):
	return [ v[0]*x, v[1]*x, v[2]*x ]

def substraction(v1,v2):
	return [ v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2] ]

def vectorDivide(v,x):
	return [ v[0]/x, v[1]/x, v[2]/x ]

def brake(v):
	return [-v[0],v[1],-v[2]]


def vectorLength(vector):
	return sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))

def randomBinomial():
	return random() - random()

def orientationAsVector(v):
	return [sin(v),0,cos(v)]


# Seek/Flee Algorithm
def seeknflee(agent, target, flag):

	global maxAcceleration

	# Create the structure for output
	steering = SteeringOutput()

	# Get the direction of the target
	if flag == "seek":
		steering.linear = substraction(target.position,agent.position)
	elif flag == "flee":
		steering.velocity = substraction(agent.position,target.position)

	# Give full acceleration is along this direction
	steering.linear = normalize(steering.linear)
	steering.linear = vectorTimes(steering.linear,maxAcceleration)

	# Output the steering
	steering.angular = 0
	return steering

def arrive(agent, target):

	global maxSpeed, maxAcceleration

	# Holds the satisfaction radius
	targetRadius = 3
	slowRadius = 15

	# Holds the time to target constant
	timeToTarget = 0.1

	# Create the structure for output
	steering = SteeringOutput()

	# Get the direction to the target
	direction = substraction(target.position,agent.position)
	distance = vectorLength(direction)

	# Check if we are there, return no steering
	if distance < targetRadius:
		return None

	# If we are outside the slowRadius, then go max speed
	if distance > slowRadius:
		targetSpeed = maxSpeed
	# Otherwise calculate a scaled speed
	else:
		targetSpeed = maxSpeed * distance / slowRadius


	# The target velocity combines speed and direction
	targetVelocity = direction
	targetVelocity = normalize(targetVelocity)
	targetVelocity = vectorTimes(targetVelocity,targetSpeed)

	# Acceleration tries to get to the target velocity
	steering.linear = substraction(targetVelocity,agent.velocity)
	steering.linear = vectorDivide(steering.linear,timeToTarget)

	# Check if the acceleration is too fast
	if vectorLength(steering.linear) > maxAcceleration:
		steering.linear = normalize(steering.linear)
		steering.linear = vectorTimes(steering.linear,maxAcceleration)

	# Output the steering
	steering.angular = 0
	return steering

################### Parte de Lili ####################

