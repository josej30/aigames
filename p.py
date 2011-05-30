from ia.aStar import *

a = pathfindAStar()

print a[0].fromNode.node
for i in a:
    print i.toNode.node
