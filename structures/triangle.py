class Triangle:
	vertex1 = ()
	vertex2 = ()
	vertex3 = ()

	def __init__(self,a,b,c):
		self.vertex1 = a
    		self.vertex2 = b
    		self.vertex3 = c
    	def centerOfMass(self):
		g = [0,0]
    		G[0] = (self.vertex1[0] + self.vertex2[0] + self.vertex3[0])/3
    		G[1] = (self.vertex1[1] + self.vertex3[1] + self.vertex3[1])/3
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
