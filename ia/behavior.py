from structures.BehaviorAndWeight import *
from structures.triangle import *
from misc.vector3 import *
from ia.steeringBehaviours import *
from ia.collisions import *
from ia.aStar import *
from ia.shot import *

# Matrix of the first map
m = [[-1]*60 for x in xrange(60)]
m[0][1] = 1
m[1][0] = 1
m[0][19] = 1
m[19][0] = 1
m[1][2] = 1
m[2][1] = 1
m[2][3] = 1
m[3][2] = 1
m[3][4] = 1
m[4][3] = 1
m[4][5] = 1
m[5][4] = 1
m[4][17] = 1
m[17][4] = 1
m[5][6] = 1
m[6][5] = 1
m[6][7] = 1
m[7][6] = 1
m[7][14] = 1
m[14][7] = 1
m[7][8] = 1
m[8][7] = 1
m[8][9] = 1
m[9][8] = 1
m[9][10] = 1
m[10][9] = 1
m[10][11] = 1
m[11][10] = 1
m[11][12] = 1
m[12][11] = 1
m[12][13] = 1
m[13][12] = 1
m[14][15] = 1
m[15][14] = 1
m[15][16] = 1
m[16][15] = 1
m[15][24] = 1
m[24][15] = 1
m[16][17] = 1
m[17][16] = 1
m[16][23] = 1
m[23][16] = 1
m[18][19] = 1
m[19][18] = 1
m[18][20] = 1
m[20][18] = 1
m[20][21] = 1
m[21][20] = 1
m[22][23] = 1
m[23][22] = 1
m[22][37] = 1
m[37][22] = 1
m[23][24] = 1
m[24][23] = 1
m[24][25] = 1
m[25][24] = 1
m[25][34] = 1
m[34][25] = 1
m[25][26] = 1
m[26][25] = 1
m[26][27] = 1
m[27][26] = 1
m[26][33] = 1
m[33][26] = 1
m[27][28] = 1
m[28][27] = 1
m[28][29] = 1
m[29][28] = 1
m[28][13] = 1
m[13][28] = 1
m[29][30] = 1
m[30][29] = 1
m[30][31] = 1
m[31][30] = 1
m[32][31] = 1
m[31][32] = 1
m[31][46] = 1
m[46][31] = 1
m[32][33] = 1
m[33][32] = 1
m[33][34] = 1
m[34][33] = 1
m[34][35] = 1
m[35][34] = 1
m[35][44] = 1
m[44][35] = 1
m[35][36] = 1
m[36][35] = 1
m[43][36] = 1
m[36][43] = 1
m[36][37] = 1
m[37][36] = 1
m[21][38] = 1
m[38][21] = 1
m[38][39] = 1
m[39][38] = 1
m[39][41] = 1
m[41][39] = 1
m[41][40] = 1
m[40][41] = 1
m[40][59] = 1
m[59][40] = 1
m[59][58] = 1
m[58][59] = 1
m[58][57] = 1
m[57][58] = 1
m[57][56] = 1
m[56][57] = 1
m[56][55] = 1
m[55][56] = 1
m[55][42] = 1
m[42][55] = 1
m[42][43] = 1
m[43][42] = 1
m[43][44] = 1
m[44][43] = 1
m[44][45] = 1
m[45][44] = 1
m[45][52] = 1
m[52][45] = 1
m[46][47] = 1
m[47][46] = 1
m[47][48] = 1
m[48][47] = 1
m[48][49] = 1
m[49][48] = 1
m[49][50] = 1
m[50][49] = 1
m[50][51] = 1
m[51][50] = 1
m[51][52] = 1
m[52][51] = 1
m[52][53] = 1
m[53][52] = 1
m[53][54] = 1
m[54][53] = 1
m[54][55] = 1
m[55][54] = 1

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

        path = pathfindAStar(agent, foodAgent, ts, m)

        for p in path:            
            print p.toNode.node
        print "------"
            

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

    	#shot interval
    	agent.time = agent.time+1
    	if agent.time%10 ==0: 
    		agent.bullets = agent.bullets + [slow_shot(agent,1)]
    	
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
