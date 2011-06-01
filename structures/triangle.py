class Triangle:
	vertex1 = ()
	vertex2 = ()
	vertex3 = ()
	node = 0

	def __init__(self,a,b,c,d):
		self.vertex1 = a
    		self.vertex2 = b
    		self.vertex3 = c
    		self.node = d
    	def centerOfMass(self):
		G = [0,0]
    		G[0] = (self.vertex1[0] + self.vertex2[0] + self.vertex3[0])/3.0
    		G[1] = (self.vertex1[1] + self.vertex2[1] + self.vertex3[1])/3.0
    		return G

    	def orientation(self,point):
    		temp1 = (self.vertex1[0] - self.vertex3[0]) *  (self.vertex2[1] - self.vertex3[1]) 
    		temp2 = (self.vertex1[1] - self.vertex3[1]) * (self.vertex2[0] - self.vertex3[0])
    		return temp1 - temp2

    	def pointInTriangle(self,point):
		#print point
		t1 = Triangle(self.vertex1,self.vertex2,point,1)
		t2 = Triangle(self.vertex2,self.vertex3,point,2)
		t3 = Triangle(self.vertex3,self.vertex1,point,3)

		orientation_original = self.orientation(point)
		#print "original " + str(orientation_original)
    		orientation1 = t1.orientation(point)
    		#print "t1 " + str(orientation1)
    		orientation2 = t2.orientation(point)
    		#print "t2 " + str(orientation2)
    		orientation3 = t3.orientation(point)
    		#print "t3 " + str(orientation3)

    		if orientation_original>=0 and orientation1>=0 and orientation2>=0 and orientation3>=0:
    			return True
    		elif orientation_original<0 and orientation1<0 and orientation2<0 and orientation3<0:
    			return True
    		else:
    			return False

def getTriangle(triangles,point):
	for triangle in triangles:
		if triangle.pointInTriangle(point):
			return triangle
    		
    			 

#p1 = [2,0]

#p2 = [0,1]

#p3 = [-3,-2]
#t = Triangle(p1,p2,p3,1)

#p = [1/3.0,1/3.0]
#print t.pointInTriangle(p)

#print t.centerOfMass()

