from math import pow, sqrt
from misc.vector3 import *

class Segment:
    
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0

    def __init__(self,x1=0.0,y1=0.0,x2=0.0,y2=0.0):
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)

    def length(self):
        return sqrt(pow(self.x2-self.x1,2)+pow(self.y2-self.y1,2))

    # Returns True if the segment contains the point p
    def point_in_segment(self, p):

	xa = self.x1
	ya = self.y1
	xb = self.x2
	yb = self.y2
	xc = p[0]
	yc = p[1]

        return (self.same_line(xc, yc)
                and (self.between(xa, xc, xb) if xa != xb else
                     self.between(ya, yc, yb)))

    # Returns True if the point C is in the same line that A and B
    def same_line(self, xc, yc):
        f = (self.x2-self.x1)*(yc-self.y1)
        s = (xc-self.x1)*(self.y2-self.y1)
        if f == s:
            return True
        return False

    # Returns True if q is between p and r
    def between(self, p, q, r):
        if (p <= q <= r) | (r <= q <= p):
            return True
        return False
