from structures.BehaviorAndWeight import *
from structures.steeringOutput import *
from misc.vector3 import *
from ia.steeringBehaviours import *
from ia.collisions import *

# Returns the acceleration required.
def getSteering(targets,target,agent,obs,flag):

    steeringPursue = SteeringOutput()
    steeringSeek = SteeringOutput()
    steeringWander = SteeringOutput()

    if flag == "Wander":
        steeringWander = wander(face,agent,target)
    elif flag == "Pursue":
        steeringPursue = Pursue(seek,target,agent)
    elif flag == "Seek":
        steeringSeek = seek(agent, target, "seek")

    steeringObstacleAvoidance = collisionDetect2(agent,obs)
    steeringSeparation = separation(agent, targets)

    PursueWeight = 3.0
    WanderWeight = 3.0
    SeekWeight = 3.0
    ObstacleAvoidanceWeight = 10.0
    SeparationWeigth = 70.0

    if (steeringObstacleAvoidance.linear == [0,0,0]):
        PursueWeight = 3.0
        WanderWeight = 3.0
        SeekWeigth = 3.0
        SeparationWeigth = 70.0
        ObstacleAvoidanceWeight = 0.0

    # Holds a list of BehaviorAndWeight instances.
    behavior_pursue = [
        [steeringPursue,PursueWeight],
        [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
        [steeringSeparation,SeparationWeigth]
        ]
    behavior_wander = [
        [steeringWander,WanderWeight],
        [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
        [steeringSeparation,SeparationWeigth]
        ]
    behavior_seek = [
        [steeringSeek,SeekWeight],
        [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
        [steeringSeparation,SeparationWeigth]
        ]
   

    # Create the steering structure for accumulation
    steering = SteeringOutput()

    # Accumulate all accelerations
    if flag == "Pursue":
    	for behavior in behavior_pursue:
        	temp = behavior[0].scale_steering(behavior[1])
        	steering = sum_steering(steering, temp)

    elif flag == "Wander":
    	for behavior in behavior_wander:
        	temp = behavior[0].scale_steering(behavior[1])
        	steering = sum_steering(steering, temp)
        	
    elif flag == "Seek":
    	for behavior in behavior_seek:
        	temp = behavior[0].scale_steering(behavior[1])
        	steering = sum_steering(steering, temp)

    return steering
