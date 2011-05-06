def vectorTimes(v,x):
	return [ v[0]*x, v[1]*x, v[2]*x ]

def vectorPlus(v,x):
	return [ v[0]+x[0], v[1]+x[1], v[2]+x[2] ]

class Agent:
    position = [0,1,0]   # a 2 or 3D vector
    orientation = 0.0    # a single floating point value
    velocity = [0,0,0]   # another 2 or 3D vector
    rotation = 0.0       # a single floating point value

    def update (self, steering, time):
        
        # Update the position and orientation
        self.position = vectorPlus(self.position,vectorTimes(self.velocity,time))
        self.orientation += self.rotation*time

        # and the velocity and rotation
        self.velocity = vectorPlus(self.velocity,vectorTimes(steering.velocity,time))
        self.orientation += steering.rotation*time

        print self.position
