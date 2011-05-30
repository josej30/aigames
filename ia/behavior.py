from structures.BehaviorAndWeight import *
from structures.triangle import *
from misc.vector3 import *
from ia.steeringBehaviours import *
from ia.collisions import *
from ia.aStar import *

# Returns the acceleration required.
def getSteering(targets,target,agent,obs,ts,flag):

    steeringPursue = SteeringOutput()
    steeringSeek = SteeringOutput()
    steeringWander = SteeringOutput()
    steeringAstar = SteeringOutput()

    if flag == "Wander":
        steeringWander = wander(face,agent,target)
    elif flag == "Pursue":
        steeringPursue = Pursue(seek,target,agent)
    elif flag == "Seek":
        steeringSeek = seek(agent, target, "seek")
    elif flag == "Astar":
        path = pathfindAStar(agent, target, ts)
        print "begin"
        for i in path:
            print i.toNode.node
        print "end"
        #targetAstar = mapTriangle(temp[0]).centerOfMass()
        #steeringSeek = seek(agent, targetAstar, "seek")
        

    steeringObstacleAvoidance = collisionDetect2(agent,obs)
    steeringSeparation = separation(agent, targets)

    PursueWeight = 3.0
    WanderWeight = 3.0
    SeekWeight = 3.0
    AstarWeigth = 3.0
    ObstacleAvoidanceWeight = 10.0
    SeparationWeigth = 3.0

    if (steeringObstacleAvoidance.linear == [0,0,0]):
        PursueWeight = 3.0
        WanderWeight = 3.0
        SeekWeigth = 3.0
        AstarWeigth = 3.0
        SeparationWeigth = 3.0
        ObstacleAvoidanceWeight = 0.0

    # Create the steering structure for accumulation
    steering = SteeringOutput()

    # Accumulate all accelerations
    if flag == "Pursue":
        behavior_pursue = [
            [steeringPursue,PursueWeight],
            [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
            [steeringSeparation,SeparationWeigth]
            ]
    	for behavior in behavior_pursue:
        	temp = behavior[0].scale_steering(behavior[1])
        	steering = sum_steering(steering, temp)

    elif flag == "Wander":
        behavior_wander = [
            [steeringWander,WanderWeight],
            [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
            [steeringSeparation,SeparationWeigth]
            ]
        for behavior in behavior_wander:
        	temp = behavior[0].scale_steering(behavior[1])
        	steering = sum_steering(steering, temp)
        	
    elif flag == "Seek":
        behavior_seek = [
            [steeringSeek,SeekWeight],
            [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
            [steeringSeparation,SeparationWeigth]
            ]
    	for behavior in behavior_seek:
        	temp = behavior[0].scale_steering(behavior[1])
        	steering = sum_steering(steering, temp)

    elif flag == "Astar":
        behavior_astar = [
            [steeringAstar,AstarWeigth],
            [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
            [steeringSeparation,SeparationWeigth]
            ]
    	for behavior in behavior_astar:
            temp = behavior[0].scale_steering(behavior[1])
            steering = sum_steering(steering, temp)
   
    return steering
