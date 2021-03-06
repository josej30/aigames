from misc.misc import inter_rects2
from structures.segments import *
from structures.steeringOutput import *
from misc.vector3 import *

def check_physics(agents,obs,obstacle_ob):

    # Checking if the position of the agent 
    # is inside an obstacle    
    for ob in obstacle_ob:
        for agent in agents:
            if agent.position[1] > 0.0:
                if inside_ob(agent,ob):
                    agent.position[1] = ob.height
    
    r = []
    steering = SteeringOutput()
    for agent in agents:
        for ob in obs:
            # Checking for hits with an obstacle
            if agent_wall(agent,ob['seg']):
                if agent.position[1] < ob['height']:
                    temp = agent.velocity
                    if ob['normal'][0] != 0:
                        temp[0] = -temp[0]
                    elif ob['normal'][2] != 0:
                        temp[2] = -temp[2]
                    steering.linear = temp
                    r.append([agent,steering])
                    agent.velocity = temp
    return r


def agent_wall(agent,wall):

    x1 = agent.position[0]+agent.radius
    x2 = agent.position[0]-agent.radius
    y1 = agent.position[2]+agent.radius
    y2 = agent.position[2]-agent.radius
    s1 = Segment(x1,y1,x2,y1)
    s2 = Segment(x2,y1,x2,y2)
    s3 = Segment(x2,y2,x1,y2)
    s4 = Segment(x1,y2,x1,y1)

    ss = [s1,s2,s3,s4]

    for s in ss:
        inter = inter_rects2(s,wall)
        if len(inter) > 0:
            if s.point_in_segment(inter) and wall.point_in_segment(inter):
                return True

    return False



def updatePlayer(player,time,obs):
    
    steering = SteeringOutput()
    
    steering.linear[0] = -player.velocity[0]
    steering.linear[2] = -player.velocity[2]

    player.update(steering,time,obs,"auto")

    if abs(player.velocity[0]) <= 0.01:
        player.velocity[0] = 0

    if abs(player.velocity[2]) <= 0.01:
        player.velocity[2] = 0

def check_shot(bullet,agents):
	
	b = bullet.position
	for agent in agents:
		a = agent.position
		if ((a[0]-1.0) <= b[0]<= (a[0]+1)) and (a[1]-1.0) <= b[1]<= (a[1]+1) and (a[2]-1.0) <= b[2]<= (a[2]+1):
			agent.life =  agent.life -1
			
	

def check_food(food,agents):
    
    for f in food:
        b = f.centerOfMass()
        for agent in agents:
            a = agent.position
            if ((a[0]-1.0) <= b[0]<= (a[0]+1)) and (a[2]-1.0) <= b[1]<= (a[2]+1):
                agent.life = min(agent.life+(agent.maxlife*0.5),agent.maxlife)
                food.remove(f)
                break
            
            
		
def inside_ob(agent,ob):
    
    # Case when the agent is on an obstacle and it wants to fall
    if agent.position[1] == ob.height:
        if agent.position[0] > (ob.x-(ob.widex)/2.0-agent.radius)and agent.position[0] < (ob.x+(ob.widex)/2.0+agent.radius) and agent.position[2] > (ob.z-(ob.widez)/2.0-agent.radius) and agent.position[2] < (ob.z+(ob.widez)/2.0+agent.radius):
            return True

    # Case when the agent is landing on the obstacle
    # We use a epsilon of 0.1
    if agent.position[1] > ob.height-(0.1) and agent.position[1] < ob.height+(0.1) and agent.velocity[1] < 0:
        if agent.position[0] > (ob.x-(ob.widex)/2.0-agent.radius)and agent.position[0] < (ob.x+(ob.widex)/2.0+agent.radius) and agent.position[2] > (ob.z-(ob.widez)/2.0-agent.radius) and agent.position[2] < (ob.z+(ob.widez)/2.0+agent.radius):
            return True
        

    # Case when the agent is just on the obstacle
    if agent.position[1] < ob.height and agent.velocity[1] < 0:
        if agent.position[0] > (ob.x-(ob.widex)/2.0-agent.radius)and agent.position[0] < (ob.x+(ob.widex)/2.0+agent.radius) and agent.position[2] > (ob.z-(ob.widez)/2.0-agent.radius) and agent.position[2] < (ob.z+(ob.widez)/2.0+agent.radius):
            return True
        

    # Case when the agent is just on the obstacle
#    if agent.position[1] < ob.height:
#        if agent.position[0] > (ob.x-(ob.widex)/2.0)and agent.position[0] < (ob.x+(ob.widex)/2.0) and agent.position[2] > (ob.z-(ob.widez)/2.0) and agent.position[2] < (ob.z+(ob.widez)/2.0):
#            return True
        

    return False
            
        

