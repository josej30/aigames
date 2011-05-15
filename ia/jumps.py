from structures.steeringOutput import *
from structures.agents import *
from structures.jump import *
from structures.jumpPoint import *
from misc.misc import *
from misc.vector3 import *
from ia.steeringBehaviours import *

	# Holds the jump point to use
jumpPoint = JumpPoint()

    	# Keeps track of whether the jump is achievable
canAchieve = True

    	# Holds the maximum speed of the character                                  
maxSpeed = 10

   	# Holds the maximum vertical jump velocity
maxYVelocity = 10

maxVelocity = 5

   	# Retrieve the steering for this jump
t = True

def scheduleJumpAction(agent):
	if agent.position[1]==0:
		agent.velocity[1] = 25.0
	
# Retrieve the steering for this jump
def Jump(agent):
	
    
	
     	# Check if we have a trajectory, and create
     	# one if not.
     	if t:
     		print "LLamando a calcular target"
       		target = calculateTarget(agent)

	if not canAchieve:
     	# Check if the trajectory is zero
     	
     		print "no puede saltar, llamada a arrive"
     		print target.position
     		print "near"
     		print near(agent.position,target.position)
     		print near(agent.velocity,target.velocity)
       		# If not, we have no acceleration
       	 	seeknflee(agent,target,"seek")

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
def calculateTarget(agent):
	print "Calcular Target"
	t = False
     	target = Agent()

     	target.position = jumpPoint.jumpLocation


     	# Calculate the first jump time
     	sqrtTerm = sqrt(2*(-10)*jumpPoint.deltaPosition[1] + maxYVelocity*maxVelocity)

	aux = near(agent.position,target.position)-10

	if aux == 0:
		time = 0
	else:
     		time = (maxYVelocity - sqrtTerm) / aux


     	# Check if we can use it
     	if not checkJumpTime(time,target):
		
  		# Otherwise try the other time

   		time = (maxYVelocity + sqrtTerm) / -10

   		checkJumpTime(time,target)
   		
   	return target

   # Private helper method for the calculateTarget
   # function
def checkJumpTime(time, target):
	print "checkJumpTime"
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
       		
