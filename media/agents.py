from math import pow, sqrt

def vectorTimes(v,x):
	return [ v[0]*x, v[1]*x, v[2]*x ]

def vectorPlus(v,x):
	return [ v[0]+x[0], v[1]+x[1], v[2]+x[2] ]

def vectorLength(vector):
	return sqrt(pow(vector[0],2) + pow(vector[2],2))

def normalize(vector):
	factor = sqrt(pow(vector[0],2) + pow(vector[1],2) + pow(vector[2],2))
	if factor != 0:
		return [vector[0]/factor,vector[1]/factor,vector[2]/factor]
	else:
		return vector

class Agent:

	global maxSpeed

	position = [0,1,0]   # a 2 or 3D vector
	orientation = 0.0    # a single floating point value
	velocity = [0,0,0]   # another 2 or 3D vector
	rotation = 0.0       # a single floating point value
	
	def update (self, steering, maxSpeed, time):
		
		# Update the position and orientation
		self.position = vectorPlus(self.position,vectorTimes(self.velocity,time))
		self.orientation += self.rotation*time
		
		# and the velocity and rotation
		self.velocity = vectorPlus(self.velocity,vectorTimes(steering.linear,time))
		self.orientation += steering.angular*time

		# The velocity is along this direction, at full speed
		# If this is too fast, clip it to the max speed
		if vectorLength(self.velocity) > maxSpeed:
			self.velocity = normalize(self.velocity)
			self.velocity = vectorTimes(self.velocity,maxSpeed)

		print "position = " + str(self.position)
		print "velocity = " + str(self.velocity)
