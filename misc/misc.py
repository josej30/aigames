from math import sqrt, pow

def randomBinomial():
	return random() - random()

#def distanceToRadius(agent,target):
#	return sqrt(pow(target.position[0]-agent.position[0],2) + pow(target.position[2]-agent.position[2],2))

def brake(v):
	return [-v[0],v[1],-v[2]]

def two_point_distance(a,b):
	sqrt( pow(a[0]-b[0],2) + pow(a[1]-b[1],2) + pow(a[2]-b[2],2) )
