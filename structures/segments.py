from math import pow, sqrt

class Segment:
    
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self,x1=0,x2=0,y1=0,y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def length(self):
        return sqrt(pow(self.x2-self.x1,2)+pow(self.y2-self.y1,2))

    def point_in_segment(self,p1,p2):
        if (self.x1-self.x2) == 0:
            return p1 == 0
        g = ((self.y1-self.y2)/(self.x1-self.x2))
        return ((g*p1)+self.y1-(g*self.x1)-p2)==0

    
