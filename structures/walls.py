from structures.segments import *

# Class that represents a wall in the world
# and contains the data related of it

class Wall:
    
    # Coordinates of the first point
    x1 = 0
    z1 = 0

    # Coordinates of the second point
    x2 = 0
    z2 = 0

    # Height of the wall
    height = 0

    # Normal of the wall
    normal = [0,0,0]

    def __init__(self,x1,z1,x2,z2,h,n):
        self.x1 = x1
        self.x2 = x2
        self.z1 = z1
        self.z2 = z2
        self.height = h
        self.normal = n

    def get_proyection(self):
        return Segment(self.x1,self.z1,self.x2,self.z2)
        
