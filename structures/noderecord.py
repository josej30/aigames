class nodeRecord:
	node = None
	connection = ()
       	costSoFar = 10000 
       	estimatedTotalCost = 0
       	def __init__(self,a):
		self.node = a
		
	def minNode( nodeList ):
		nodeMin = nodeRecord()
		for node in nodeList:
			if node.costSoFar <= nodeMin.costSoFar:
				nodeMin = node
	return node
		
