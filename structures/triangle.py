from __future__ import division
from point import *

class Triangle:
	vertice1 = Point()
	vertice2 = Point()
	vertice3 = Point()

	def __init__(self,a,b,c):
		self.vertice1 = a
    		self.vertice2 = b
    		self.vertice3 = c
    	def centerOfMass(self):
    		G = Point()
    		G.x = (self.vertice1.x + self.vertice2.x + self.vertice3.x)
    		G.y = (self.vertice1.y + self.vertice2.y + self.vertice3.y)
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
