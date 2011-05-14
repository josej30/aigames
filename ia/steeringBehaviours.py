from math import pow , sqrt, atan2, sin, cos, fabs
from structures.kinematicSteeringOutput import *
from structures.kinematicWander import *
from structures.steeringOutput import *
from structures.agents import *
from structures.jump import *
from structures.jumpPoint import *
from misc.misc import *
from misc.vector3 import *
from random import random


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


# Seek/Flee Algorithm
def seeknflee(agent, target, flag):

	global maxAcceleration

	# Create the structure for output
	steering = SteeringOutput()

	# Get the direction of the target
	if flag == "seek":
		steering.linear = substraction(agent.position,target.position)
	elif flag == "flee":
		steering.linear = substraction(target.position,agent.position)

	# Give full acceleration is along this direction
	steering.linear = normalize(steering.linear)
	steering.linear = vectorTimes(steering.linear,maxAcceleration)

	# Output the steering
	steering.angular = 0
	return steering

def arrive(agent, target):

	global maxSpeed, maxAcceleration

	# Holds the satisfaction radius
	targetRadius = 1
	slowRadius = 20

	# Holds the time to target constant
	timeToTarget = 0.1

	# Create the structure for output
	steering = SteeringOutput()

	# Get the direction to the target
	direction = substraction(target.position,agent.position)
	distance = vectorLength(direction)

	# Check if we are there, return no steering
	if distance < targetRadius:
		return steering

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

def aligne(agent, target):


     	# Holds the max angular acceleration and rotation
     	# of the character
     	maxAngularAcceleration = .4
    	maxRotation = 10
     
     	# Holds the radius for arriving at the target
     	targetRadius = 2

     	# Holds the radius for beginning to slow down
     	slowRadius = 1

     	# Holds the time over which to achieve target speed
    	timeToTarget = .1

     	# Create the structure to hold our output
     	steering = SteeringOutput()

	
     	# Get the naive direction to the target
     	rotationDirection = target.orientation - agent.orientation

      	# Map the result to the (-pi, pi) interval
        #rotation = mapToRange(rotation)
     	rotation = atan2( agent.orientation,target.orientation)
     	rotationSize = fabs(rotationDirection)

	print rotationDirection
	print rotation
     	print rotationSize
     

    	# Check if we are there, return no steering
	if rotationSize < targetRadius:
        	return None
            	      	
        # If we are outside the slowRadius, then use
        # maximum rotation
	if rotationSize > slowRadius:
		print "maxrotation"
                
       		targetRotation = maxRotation
                
                
        # Otherwise calculate a scaled rotation
     	else:
                print "scaled rotation"
        	targetRotation = maxRotation * rotationSize / slowRadius
                            
      	# The final target rotation combines
        # speed (already in the variable) and direction
       	targetRotation = targetRotation * rotation / rotationSize
                
     	# Acceleration tries to get to the target rotation
        steering.angular = targetRotation - agent.rotation
        steering.angular = steering.angular / timeToTarget
                      
        # Check if the acceleration is too great
       	angularAcceleration = fabs(steering.angular)
                
       	if angularAcceleration > maxAngularAcceleration:
                
        	steering.angular = steering.angular / angularAcceleration
                
   		steering.angular = steering.angular * maxAngularAcceleration
                
        # Output the steering
      	steering.linear = [0,0,0]
   	return steering

def VelocityM(agent,target):

	# Holds the time to target constant
	timeToTarget = 0.1
	
	# Create the structure to hold our output
	steering = SteeringOutput()
	
	# Acceleration tries to get to the target velocity
	substraction(target.velocity,agent.velocity)
	steering.linear = vectorDivide(steering.linear,timeToTarget)

	# Check if the acceleration is too fast
	if vectorLength(steering.linear) > maxAcceleration:
		steering.linear = normalize(steering.linear)
		steering.linear = vectorTimes(steering.linear,maxAcceleration)
		

     	# Output the steering
     	steering.angular = 0

     	return steering

def Pursue(seeknflee,target_p, agent_p,):

	print "Pursue"
     	# Holds the maximum prediction time
     	maxPrediction = 1
     	
  

     	# OVERRIDES the target data in seek (in other words
     	# this class has two bits of data called target:
     	# Seek.target is the superclass target which
     	# will be automatically calculated and shouldnt
     	# be set, and Pursue.target is the target were
     	# pursuing).

     


     	# ... Other data is derived from the superclass ...

       # 1. Calculate the target to delegate to seek
       # Work out the distance to target
       	direction = substraction(target_p.position , agent_p.position)
       	distance = vectorLength(direction)

       # Work out our current speed
       	speed = vectorLength(agent_p.velocity)

       # Check if speed is too small to give a reasonable
       # prediction time
       	if speed <= distance / maxPrediction:
       
       		prediction = maxPrediction

       # Otherwise calculate the prediction time
       	else:

      		prediction = distance / speed

       # Put the target together
       
       	target_p.position = addition(target_p.position,vectorTimes(target_p.velocity , prediction))
       	

       # 2. Delegate to seek
       	return arrive(agent_p, target_p)

def face(aligne, agent, target):
   	# Work out the direction to target
   	#print target.position
   	#print agent.position
	direction = substraction(target.position,agent.position)

   	# Check for a zero direction, and make no change if so
   	if vectorLength(direction) == 0:
   		return target

   	# Put the target together
	target.orientation = atan2(-direction[0],direction[2])

   	# 2. Delegate to align

   	return aligne(agent, target)

def lookWhereYoureGoing(aligne,agent, target):

   	# Check for a zero direction, and make no change if so
   	if vectorLength(agent.velocity) == 0: return

   	# Otherwise set the target based on the velocity
   	target.orientation = atan2(-agent.velocity[0], agent.velocity[2])

   	# 2. Delegate to align
   	return aligne(agent,target)

def wander(face,agent,target):
 
 
     	# Holds the radius and forward offset of the wander
     	# circle.
     	wanderOffset = 4.0
     	wanderRadius = 4.0
 
     	# Holds the maximum rate at which the wander orientation
     	# can change 
     	wanderRate = 10

     	# Holds the current orientation of the wander target
     	wanderOrientation = 0


     	# Holds the maximum acceleration of the character
     	maxAcceleration = 2

     	# Again we dont need a new target
     	# ... Other data is derived from the superclass ...
      	# 1. Calculate the target to delegate to face
       	# Update the wander orientation
       	wanderOrientation += randomBinomial() * wanderRate

                                            
   	# Calculate the combined target orientation
   	targetOrientation = wanderOrientation + agent.orientation

   	# Calculate the center of the wander circle
   	target.position = addition(agent.position,  vectorTimes(orientationAsVector(agent.orientation),wanderOffset))

   	# Calculate the target location
   	target.position =  addition(target.position, vectorTimes(orientationAsVector(targetOrientation),wanderRadius))

   	# 2. Delegate to face
   	steering = face(aligne, agent, target)

   	# 3. Now set the linear acceleration to be at full
   	# acceleration in the direction of the orientation

   	steering.linear =vectorTimes(orientationAsVector(agent.orientation), maxAcceleration)

   	# Return it
   	
   	return steering
       		



