class Agent:
    position = [0,1,0]   # a 2 or 3D vector
    orientation = 0.0    # a single floating point value
    velocity = [0,0,0]   # another 2 or 3D vector
    rotation = 0.0       # a single floating point value

    def update (self, steering, time):
        
        # Update the position and orientation
        self.position += self.velocity * time
        self.orientation += self.rotation * time

        # and the velocity and rotation
        self.velocity += steering.linear * time
        self.orientation += steering.angular * time
