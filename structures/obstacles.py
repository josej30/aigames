from structures.segments import *

# Definition of an obstacle

class Obstacle:
    
    x = 0
    y = 0
    z = 0
    widex = 0
    widez = 0
    height = 0

    # Constructor
    def __init__(self,x,y,z,widex,widez,height):
        self.x = x
        self.y = y
        self.z = z
        self.widex = widex
        self.widez = widez
        self.height = height

    # Return an array with the segments that represents
    # the walls of the obstacle.
    # [left,up,right,bottom]
    def segments(self):
        return [ 
            Segment(self.x-self.widex,self.z-self.widez,self.x-self.widex,self.z+self.widez) ,
            Segment(self.x-self.widex,self.z+self.widez,self.x+self.widex,self.z+self.widez) ,
            Segment(self.x+self.widex,self.z+self.widez,self.x+self.widex,self.z-self.widez) ,
            Segment(self.x+self.widex,self.z-self.widez,self.x-self.widex,self.z-self.widez)
            ]

    # Return an array with the normals of the obstacle.
    # [left,up,right,bottom]
    def normals(self):
        return [
            [-1,0,0],
            [0,0,1],
            [1,0,0],
            [0,0,-1]
            ]
