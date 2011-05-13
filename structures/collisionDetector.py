from media.graphics import *
from misc.misc import *
from misc.vector3 import *
from structures.segments import *

def getCollision(position, moveAmount, obs):

    if (position[0]-moveAmount[0]) == 0:
        m1 = 1
    else:
        m1 = ((position[2]-moveAmount[2])/(position[0]-moveAmount[0]))
    b1 = moveAmount[2] - (m1*moveAmount[0])

    for seg in obs:
            
        if (seg.x1-seg.x2) == 0:
            m2 = 1
        else:
            m2 = ((seg.y1-seg.y2)/(seg.x1-seg.x2))
        b2 = seg.y2 - (m2*seg.x2)
        
        if (m2-m1) == 0:
            interx = 0
        else:
            interx = ((b1-b2)/(m2-m1))
        intery = (m1*interx)+b1
        
        if seg.point_in_segment(interx,intery):
            print "* El punto " + str(interx) + "," + str(intery) + " se encuentra contenido en el segmento " + str(seg.x1) + "," + str(seg.y1) + " - " + str(seg.x2) + "," + str(seg.y2)
            print "---------- COLISIOOOOON -----------"
            
