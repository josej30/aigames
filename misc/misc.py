def randomBinomial():
	return random() - random()

def distanceToRadius(agent,target):
	return sqrt(pow(target.position[0]-agent.position[0],2) + pow(target.position[2]-agent.position[2],2))

def brake(v):
	return [-v[0],v[1],-v[2]]



