from math import sqrt, pow

def randomBinomial():
	return random() - random()

#def distanceToRadius(agent,target):
#	return sqrt(pow(target.position[0]-agent.position[0],2) + pow(target.position[2]-agent.position[2],2))

def brake(v):
	return [-v[0],v[1],-v[2]]

def two_point_distance(a,b):
	sqrt( pow(a[0]-b[0],2) + pow(a[1]-b[1],2) + pow(a[2]-b[2],2) )

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
    

