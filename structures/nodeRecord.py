class nodeRecord:
	node = 0
	connection = ()
       	costSoFar = 10000 
       	estimatedTotalCost = 0
       	def __init__(self,a):
		self.node = a

	def estimate(self, xDest, yDest):
        	xd = xDest - self.xPos
        	yd = yDest - self.yPos
        	# Euclidian Distance
        	d = math.sqrt(xd * xd + yd * yd)
        	return d
	
		
