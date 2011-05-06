from agents import *
from kinematicSteeringOutput import *
from math import pow , sqrt, atan2

maxSpeed = 15

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
	return sqrt(pow(vector[0],2) + pow(vector[2],2))
	#return [sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))]
	
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

# Seek/Flee Algorithm
def seeknflee(agent, target, flag):

	global maxSpeed

	#Create the structure for output
	steering = KinematicSteeringOutput()

	#Get the direction of the target
	if flag == "seek":
		steering.velocity = substraction(target.position,agent.position)
	elif flag == "flee":
		steering.velocity = substraction(agent.position,target.position)

	# The velocity is along this direction, at full speed
#	steering.velocity = normalize(steering.velocity)
	steering.velocity = [1,0,1]
   	steering.velocity = vectorTimes(steering.velocity,maxSpeed)

     	# Face in the direction we want to move
	agent.orientation = getNewOrientation(agent.orientation, steering.velocity)

	# Output the steering
	steering.rotation = 0

	return steering

def arrive(agent, target):

	global maxSpeed

	# Holds the satisfaction radius
	radius = 20

	# Holds the time to target constant
	timeToTarget = 100000

	# Create the structure for output
	steering = KinematicSteeringOutput()

	# Get the direction to the target
	steering.velocity = substraction(target.position,agent.position)

	# Check if we're within radius
	if distanceToRadius(agent,target) > radius:
		print distanceToRadius(agent,target)
		# We can return no steering request
		return None
	
	print "Dentro del radio"

	# We need to move to our target, we'd like to
	# get there in timeToTarget seconds
   	steering.velocity = vectorDivide(steering.velocity,timeToTarget)

	# If this is too fast, clip it to the max speed
	if normalize(steering.velocity) > maxSpeed:
		print "holaaaa"
		steering.velocity = [1,0,1]
		steering.velocity = vectorTimes(steering.velocity,maxSpeed)

	# Face in the direction we want to move
	agent.orientation = getNewOrientation(agent.orientation, steering.velocity)

	# Output the steering
	steering.rotation = 0

	steering.velocity = brake(steering.velocity)

	return steering

