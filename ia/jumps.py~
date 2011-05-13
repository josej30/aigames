from structures.steeringOutput import *
from structures.agents import *
from structures.jump import *
from structures.jumpPoint import *
from misc.misc import *
from misc.vector3 import *

	# Holds the jump point to use
jumpPoint = JumpPoint()

    	# Keeps track of whether the jump is achievable
canAchieve = False

    	# Holds the maximum speed of the character                                  
maxSpeed = 8

   	# Holds the maximum vertical jump velocity
maxYVelocity = 10

maxVelocity = 7

   	# Retrieve the steering for this jump
t = True

def scheduleJumpAction(agent,target):
	agent.velocity[1] = 5.0
	
# Retrieve the steering for this jump
def Jump(agent):
	
    
	
     	# Check if we have a trajectory, and create
     	# one if not.
     	if t:
     		print "LLamando a calcular target"
       		target = calculateTarget()

     	# Check if the trajectory is zero
     	if not canAchieve:
     		print "No hay aceleracion"
       		# If not, we have no acceleration
       		return SteeringOutput()

     	# Check if we ve hit the jump point (character
     	# is inherited from the VelocityMatch base class)
     	if near(agent.position,target.position) and near(agent.velocity,target.velocity):

       		# Perform the jump, and return no steering
       		# (we re airborne, no need to steer).
		print "Agendar salto"
       		scheduleJumpAction(agent)

       		return SteeringOutput()


     	# Delegate the steering
     	return VelocityM(agent,target)


# Works out the trajectory calculation
def calculateTarget():
	print "Calcular Target"
	t = False
     	target = Agent()

     	target.position = jumpPoint.jumpLocation


     	# Calculate the first jump time
     	sqrtTerm = sqrt(20*jumpPoint.deltaPosition[1] + maxYVelocity*maxVelocity)

     	time = (maxYVelocity - sqrtTerm) / 10


     	# Check if we can use it
     	if not checkJumpTime(time,target):
		
  		# Otherwise try the other time

   		time = (maxYVelocity + sqrtTerm) / 10

   		checkJumpTime(time,target)
   		
   	return target

   # Private helper method for the calculateTarget
   # function
def checkJumpTime(time, target):

     	# Calculate the planar speed
     	vx = jumpPoint.deltaPosition[0] / time

     	vz = jumpPoint.deltaPosition[2] / time

     	speedSq = vx*vx + vz*vz

     	# Check it
     	if speedSq < maxSpeed*maxSpeed:


       		# We have a valid solution, so store it
       		target.velocity[0] = vx

       		target.velocity[2] = vz

       		canAchieve = True
       		
