from misc.vector3 import *

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
    		
    	def pointInTriangle(self,p):
    		t = self.organize()
    		v1 = t.vertex1
    		v2 = t.vertex2
    		v3 = t.vertex3

		v = [v1,v2,v3]
    		for i in range(2):
    			(x1,y1) = substraction1(v[i],v[i+1])
    			(x11,y11) = substraction1(p,v[i])
    			if determinat((x1,y1),(x11,y11))>0:
    				#print "determinante" + str(determinat((x1,y1),(x11,y11)))
    				return False
    		(x1,y1) = substraction1(v[2],v[0])
    		(x11,y11) = substraction1(p,v[2])
    		if determinat((x1,y1),(x11,y11))>0:
    			#print "determinante" + str(determinat((x1,y1),(x11,y11)))
    			return False
    		else:
    			return True
    	
    	def organize(self):
    		v1 = self.vertex1
    		v2 = self.vertex2
    		v3 = self.vertex3
		
		if v1[0] < v2[0]:
			if v2[0]< v3[0]:	
				temp = max_y(v2,v1)	
				return Triangle(v3,temp[0],temp[1],self.node) 
			elif v2[0] > v3[0]:
				temp = max_y(v3,v1)
				return Triangle(v2,temp[0],temp[1],self.node) 
				#return v2.append(max_y(v3,v1))
			elif v2[0]==v3[0]:
				if v3[1]<= v2[1]:
					temp = max_y(v2,v1)	
					return Triangle(v3,temp[0],temp[1],self.node) 
					#return v3.append(max_y(v2,v1))
				else:
					temp = max_y(v3,v1)
					return Triangle(v2,temp[0],temp[1],self.node) 
					#return v2.append(max_y(v3,v1))
		elif v1[0] > v2[0]:
			if v1[0]< v3[0]:
				temp = max_y(v2,v1)	
				return Triangle(v3,temp[0],temp[1],self.node)
				#return v3.append(max_y(v2,v1))
			elif v1[0] > v3[0]:
				temp = max_y(v2,v3)	
				return Triangle(v1,temp[0],temp[1],self.node)
				#return v1.append(max_y(v3,v2))
			elif v1[0]==v3[0]:
				if v3[1]<= v1[1]:
					temp = max_y(v2,v1)	
					return Triangle(v3,temp[0],temp[1],self.node) 
					#return v3.append(max_y(v2,v1))
				else:
					temp = max_y(v2,v3)	
					return Triangle(v1,temp[0],temp[1],self.node)
					#return v1.append(max_y(v3,v2))
		elif v1[0]==v2[0]:
			if v1[0]>= v3[0]:
				temp = max_y(v2,v3)	
				return Triangle(v1,temp[0],temp[1],self.node)
				#return v1.append(max_y(v3,v2))
			else:
				temp = max_y(v2,v1)	
				return Triangle(v3,temp[0],temp[1],self.node)
				#return v3.append(max_y(v2,v1))
			

	
def getTriangle(triangles,point):
	for triangle in triangles:
		if triangle.pointInTriangle(point):
			return triangle



