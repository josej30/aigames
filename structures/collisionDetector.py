from media.graphics import *
from misc.misc import *
from misc.vector3 import *
from structures.segments import *
from structures.Collision import *
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
                
                print " Colision en el punto (" + str(inter[0]) + "," + str(inter[1]) + ")"

                collisions.append(Collision([inter[0],0,inter[1]],ob['normal']))

    return priorCollisions(collisions,position)
        
            
# Returns the intersection of the rects using the 
# format (coord_x,coord_y)
def inter_rects(p,q):
    
    p_vert = False 
    q_vert = False

    if (p.x1-p.x2) == 0:
        pm = 1
        pb = 0
        p_vert = True
    else:
        pm = ((p.y1-p.y2)/(p.x1-p.x2))
        pb = p.y2 - (pm*p.x2)


    if (q.x1-q.x2) == 0:
        qm = 1
        qb = 0
        q_vert = True
    else:
        qm = ((q.y1-q.y2)/(q.x1-q.x2))
        qb = q.y2 - (qm*q.x2)

    if p_vert:
        return [p.x1,(qm*p.x1)+qb]

    if q_vert:
        return [q.x1,(pm*q.x1)+pb]
        
    if (pm-qm) == 0:
        return []
        #print "Son paralelas"
    else:
        if ~p_vert & ~q_vert:
            interx = ((pb-qb)/(qm-pm))
        if p_vert:
            interx = p.x1
        if q_vert:
            interx = q.x1
        intery = (pm*interx)+pb

        # print "pb = " + str(pb)
        # print "qb = " + str(qb)
        # print "pm = " + str(pm)
        # print "qm = " + str(qm)
        # print "interx = " + str(interx)
        # print "intery = " + str(intery)

        return [interx,intery]

def inter_rects2(p,q):

    A1 = p.y2 - p.y1
    B1 = p.x1 - p.x2
    C1 = A1*p.x1 + B1*p.y1

    A2 = q.y2 - q.y1
    B2 = q.x1 - q.x2
    C2 = A2*q.x1 + B2*q.y1

    det = A1*B2 - A2*B1
    if det == 0:
        return []
    else:
        x = (B2*C1 - B1*C2)/det
        y = (A1*C2 - A2*C1)/det

    return [x,y]
    

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
        


    
