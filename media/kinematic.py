from agents import *
from kinematicSteeringOutput import *
from math import pow , sqrt, atan2

def getNewOrientation(currentOrientation, velocity):

	# Make sure we have a velocity
	if velocity.len > 0:

	# Calculate orientation using an arc tangent of
 	# the velocity components.
 		return atan2(-velocity[0],velocity[2])
 	# Otherwise use the current orientation

   	else:
   		return currentOrientation



def normalize(vector):
	return sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))
	
def substraction(v1,v2):
	return [ v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2] ]

def seek(agent, target):

	#Create the structure for output
	steering = KinematicSteeringOutput()

	#Get the direction of the target
	steering.velocity = substraction(target.position,agent.position)

	#The velocity is along this direction, at full speed
   	steering.velocity = normalize(steering.velocity)
   	steering.velocity *= maxSpeed

     	# Face in the direction we want to move
	agent.orientation = getNewOrientation(agent.orientation, steering.velocity)

	# Output the steering
	steering.rotation = 0

	return steering




