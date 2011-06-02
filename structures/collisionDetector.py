from media.graphics2 import *
from misc.misc import *
from misc.vector3 import *
from structures.segments import *
from structures.Collision import *
from misc.misc import inter_rects2
import time

def getCollision(position, moveAmount, obs):

    ray = Segment(position[0],position[2],moveAmount[0],moveAmount[2])

    collisions = []

    # For each obstacle in the world, we search for intersections
    # between the ray vector and the obstacle
    for ob in obs:

        inter = inter_rects2(ray,ob['seg'])

        # If there was an intersection
        if len(inter) > 0:
            
            # We determine wheter or not the point 
            # is contained into the segment
            if ray.point_in_segment(inter) and ob['seg'].point_in_segment(inter):
                
#                print " Colision en el punto (" + str(inter[0]) + "," + str(inter[1]) + ")"

                collisions.append(Collision([inter[0],0,inter[1]],ob['normal']))

    return priorCollisions(collisions,position)
        
            
def priorCollisions(colis,pos_agent):

    n = len(colis)

    # In case we have no collisions
    if  n == 0:
        return None

    # In case we have just one collision
    if n == 1:
        return colis[0]

    # In case we have many collisions, return the nearest
    # to the agent

    d = two_point_distance(colis[0].position,pos_agent)
    c = 0
    for i in range(1,n):
        new_d = two_point_distance(colis[i].position,pos_agent)
        if new_d < d:
            d = new_d
            c = i

    return colis[c]
        


    
