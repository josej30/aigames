from media.graphics import *
from misc.misc import *
from misc.vector3 import *
from structures.segments import *
from structures.Collision import *

def getCollision(position, moveAmount, obs):

    ray = Segment(position[0],position[2],moveAmount[0],moveAmount[2])

    for seg in obs:
        inter = inter_rects(ray,seg)

        # If there was an intersection
        if len(inter) > 0:
            
            # We determine wheter or not the point 
            # is contained into the segment
            if ray.point_in_segment(inter):
                
                print " Colision inminente en el punto (" + str(inter[0]) + "," + str(inter[1]) + ")"

                return Collision(position,[1,0,0])

    return None
                

        
            
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
