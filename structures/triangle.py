from __future__ import division
from point import *

class Triangle:
	vertex1 = Point() 
	vertex2 = Point()
	vertex3 = Point()

	def __init__(self,a,b,c):
		self.vertex1 = a
    		self.vertex2 = b
    		self.vertex3 = c
    	def centerOfMass(self):
    		G = Point()
    		G.x = (self.vertex1.x + self.vertex2.x + self.vertex3.x)/3
    		G.y = (self.vertex1.y + self.vertex3.y + self.vertex3.y)/3
    		return G
#p1 = Point()
#p1.x = 2
#p1.y = 0
#p2 = Point()
#p2.x = 0
#p2.y = 1
#p3 = Point()
#p3.x = -3
#p3.y = -2
#t = Triangle(p1,p2,p3)
#t.centerOfMass()
