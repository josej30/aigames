from misc.misc import inter_rects2
from structures.segments import *
from structures.steeringOutput import *
from misc.vector3 import *

def check_physics(agents,obs):

    for agent in agents:
        for ob in obs:
            if agent_wall(agent,ob['seg']):
                agent.velocity = ob['normal']
                return True
    return False
            


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
            
