from math import pow , sqrt, atan2, sin, cos, fabs
from random import random

def normalize(vector):
	factor = sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))
	if factor != 0:
		return [vector[0]/factor,vector[1]/factor,vector[2]/factor]
	else:
		return vector

def vectorPlus(v,x):
	return [ v[0]+x[0], v[1]+x[1], v[2] + x[2] ]
	
def vectorTimes(v,x):
	return [ v[0]*x, v[1]*x, v[2]*x ]

def substraction(v1,v2):
	return [ v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2] ]

def airSubstraction(v1,v2):
	return [ 0, -10, 0 ]

def addition(v1,v2):
	return [ v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2] ]

def vectorDivide(v,x):
	return [ v[0]/x, v[1]/x, v[2]/x ]

def vectorLength(vector):
	return sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))

def orientationAsVector(v):
	return [sin(v),0,cos(v)]

def randomBinomial():
	return random() - random()

def dotProduct(v1,v2):
	return (v1[0]*v2[0]) + (v1[1]*v2[1]) + (v1[2]*v2[2])

def similarity(v1,v2):
	if vectorLength(v1) * vectorLength(v2) == 0:
		return 0
	else:
		return dotProduct(v1,v2) / (vectorLength(v1) * vectorLength(v2))

def near (v1,v2):
	if similarity(v1,v2)> .2 :
		return True
	else:
		return False
