from structures.triangle import *
from misc.vector3 import *
p1 = [-2,0]

p2 = [0,2]

p3 = [2,0]
point = [2.5,.5]
t = Triangle(p1,p2,p3,1)

p = t.organize()
print p.vertex1
print p.vertex2
print p.vertex3
print p.node
print t.pointInTriangle(point)
#print t.pointInTriangle(p)

#print t.centerOfMass()
