from structures.nodeRecord import *
from structures.Connection import *
def minNode( nodeList ):
		nodeMin = nodeRecord(0)
		for node in nodeList:
			if node.costSoFar <= nodeMin.costSoFar:
				nodeMin = node
		return node
		
def pathfindAStar():
	
	node0 = nodeRecord(0)
	node1 = nodeRecord(1)
	node2 = nodeRecord(2)
	node3 = nodeRecord(3)
	node4 = nodeRecord(4)
	node5 = nodeRecord(5)
	node6 = nodeRecord(6)

	goal = node6
	star = node0
	
	nodes = [node0,node1,node2,node3,node4,node5,node6]
	
	graph = [ [-1,2,4,-1,-1,-1,-1],
		[-1,-1,-1,3,4,-1,-1],
		[-1,-1,-1,-1,6,-1,-1],
		[-1,-1,-1,-1,-1,-1,6],
		[-1,-1,-1,-1,-1,2,3],
		[-1,-1,-1,-1,-1,-1,3],
		[-1,-1,-1,-1,-1,-1,-1]
	
	] 
     	# Initialize the record for the start node
     	startRecord = nodeRecord(0)
     	startRecord.connection = None
     	startRecord.costSoFar = 0.0

   	startRecord.estimatedTotalCost = 0.0#node0.estimate(node6)


   	# Initialize the openList and closed lists
   	openList = []
   	
   	openList.append(startRecord)

   	closed = []

	
   	# Iterate through processing each node
	current = []
   	while len(openList) > 0:
   		
   		print  len(openList)
   		
		connections = []
		
     		# Find the smallest element in the openList list
     		# (using the estimatedTotalCost)

     		current = minNode(openList)

     		# If it is the goal node, then terminate
     		if current.node == goal.node: break

     		# Otherwise get its outgoing connections
     		#connections = graph.getConnections(current)
     		for index in range(0,6):
     		
     			if graph[current.node][index]!=-1:
     			
     				new_connection = Connection()
     				new_connection.cost = graph[current.node][index]
     				new_connection.fromNode = current.node
     				new_connection.toNode = nodes[index] 
     				connections.append(new_connection)

     		# Loop through each connection in turn
     		for connection in connections:
     			print connection.cost


       			# Get the cost estimate for the end node
       			endNode = connection.getToNode()
       			print "Nodo al que voy"
       			print endNode.node
       			print "nodo del que vengo"
       			print connection.getFromNode()

       			endNodeCost = current.costSoFar + connection.getCost()


       			# If the node is closed we may have to
       			# skip, or remove it from the closed list.
       			try:
       				i = closed.index(endNode)
   			except ValueError:
       				i = -1

       			try:
       				j = openList.index(endNode)
   			except ValueError:
       				j = -1

			print i
       			if i>=0:
				print "index closed"

	 			# Here we find the record in the closed list
	 			# corresponding to the endNode.
	 			endNodeRecord = closed[i]

	 			# If we didn't find a shorter route, skip
	 			if endNodeRecord.costSoFar <= endNodeCost:
	   				continue;


		 		# Otherwise remove it from the closed list
		 		closed.remove(endNodeRecord)
	   			# We can use the node's old cost values
	   			# to calculate its heuristic without calling
	   			# the possibly expensive heuristic function

	   			endNodeHeuristic = 0.0#endNodeRecord.cost - endNodeRecord.costSoFar
	   		   # Skip if the node is openList and we've not

   			# found a better route
   			elif j>=0:

     				# Here we find the record in the openList list
     				# corresponding to the endNode.
     				endNodeRecord = openList[j]
     				   # If our route is no better, then skip

   				if endNodeRecord.costSoFar <= endNodeCost:

			     		continue;
			      	# We can use the node's old cost values
			      	# to calculate its heuristic without calling

			      	# the possibly expensive heuristic function
			 
			      	endNodeHeuristic = 0.0#endNodeRecord. - endNodeRecord.costSoFar
			 
			 
			# Otherwise we know we've got an unvisited
			# node, so make a record for it
			 
			else:
			      	endNodeRecord = endNode
			 
			      	# We'll need to calculate the heuristic value
			      	# using the function, since we dont have an
			      	# existing record to use
			      	endNodeHeuristic = 0.0 #heuristic.estimate(endNode)
			 
			# We're here if we need to update the node
			# Update the cost, estimate and connection
			endNodeRecord.cost = endNodeCost
			 
			endNodeRecord.connection = connection
			 
			endNodeRecord.estimatedTotalCost = endNodeCost + endNodeHeuristic


			try:
       				j1 = openList.index(endNode)
   			except ValueError:
       				j1 = -1
			# And add it to the openList list
		
			if j1 != -1:
	    			openList.append(endNodeRecord)

		try:
       			j2 = openList.index(current)
   		except ValueError:
       			j2 = -1
	

		# We've finished looking at the connections for
		# the current node, so add it to the closed list
		# and remove it from the openList list
		print "j2"
		if j2 >= 0:
			openList.remove(current)
		closed.append(current)
		

		# We're here if we've either found the goal, or
		# if we've no more nodes to search, find which.
	
	if current.node != goal.node:
		print "return"

	# We've run out of nodes without finding the
	# goal, so there's no solution

	
		return None


    	else:
    		print "en el path"

      		# Compile the list of connections in the path
      		path = []


      		# Work back along the path, accumulating
      		# connections

      		while current.node != star:
			path.append( current.connection)
			current = current.connection.getFromNode()


      	# Reverse the path, and return it
	print "el camino"
	print path
	return path.reverse()

