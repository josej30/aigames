from structures.BehaviorAndWeight import *
from structures.triangle import *
from misc.vector3 import *
from ia.steeringBehaviours import *
from ia.collisions import *
from ia.aStar import *
from ia.shot import *

# Returns the acceleration required.
def getSteering(targets,target,agent,obs,ts,food):

    flag = agent.state

    steeringPursue = SteeringOutput()
    steeringSeek = SteeringOutput()
    steeringFlee = SteeringOutput()
    steeringWander = SteeringOutput()
    steeringAstar = SteeringOutput()

    if flag == "Wander":
        steeringWander = wander(face,agent)

    elif flag == "Pursue":
        steeringPursue = Pursue(target,agent)

    elif flag == "Seek":
        steeringSeek = seek(agent, target, "seek")

    elif flag == "Flee":
        steeringFlee = seek(agent, target, "flee")

    elif flag == "Astar":
        
        # Finding the closest food
        closestDist = 99999999999999
        closest = None
        for f in food:
            c = f.centerOfMass()
            euclid = sqrt((pow((agent.position[2]-c[1]),2.0)) + (pow((agent.position[0]-c[0]),2.0)) )
            if euclid < closestDist:
                closestDist = euclid
                closest = f
            
        foodAgent = Agent()
        foodAgent.position[0] = closest.centerOfMass()[0]
        foodAgent.position[2] = closest.centerOfMass()[1]

        path = pathfindAStar(agent, foodAgent, ts)
        triag = ts[0]
        if path != [] and path != -1:
            for i in ts:
        	if i.node==path[0].toNode.node:
                    triag = i
    
            targetAstar = triag.centerOfMass() 
            nodeTarget = Agent()
            nodeTarget.position[0] = targetAstar[0]
            nodeTarget.position[2] = targetAstar[1]	
            steeringAstar = onlyseek(nodeTarget, agent)
        
    steeringObstacleAvoidance = collisionDetect2(agent,obs)
    steeringSeparation = separation(agent, targets)

    PursueWeight = 3.0
    WanderWeight = 3.0
    SeekWeight = 3.0
    FleeWeight = 3.0
    AstarWeigth = 3.0
    ObstacleAvoidanceWeight = 10.0
    SeparationWeigth = 150.0

    if (steeringObstacleAvoidance.linear == [0,0,0]):
        ObstacleAvoidanceWeight = 0.0

    # Create the steering structure for accumulation
    steering = SteeringOutput()

    # Accumulate all accelerations
    if flag == "Pursue":
    	print "PURSUE"
    	agent.bullets = target.bullets + [slow_shot(agent)]
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

    elif flag == "Flee":
        behavior_flee = [
            [steeringFlee,FleeWeight],
            [steeringObstacleAvoidance,ObstacleAvoidanceWeight],
            [steeringSeparation,SeparationWeigth]
            ]
    	for behavior in behavior_flee:
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
    #target.position = addition(target.position,vectorTimes(target.velocity , 1))
    return steering
