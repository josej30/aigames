from misc.vector3 import *
class JumpPoint: 
 
     	# The position of the jump point
     	jumpLocation = [0, 0 , 0]
 
 
     	# The position of the landing pad
     	landingLocation = [10, 0, 0]
 
 
     	# The change in position from jump to landing
     	# This is calculated from the other values
     	deltaPosition = substraction(jumpLocation,landingLocation) 


