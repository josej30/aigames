from structures.nodeRecord import *
from structures.Connection import *
from structures.triangle import *

def minNode( nodeList ):
	nodeMin = nodeRecord(0)
	for node in nodeList:
		if node.costSoFar <= nodeMin.costSoFar:
			nodeMin = node
	return nodeMin
		
def pathfindAStar(enemy, player):

	node0 = nodeRecord(0)
	node1 = nodeRecord(1)
	node2 = nodeRecord(2)
	node3 = nodeRecord(3)
	node4 = nodeRecord(4)
	node5 = nodeRecord(5)
	node6 = nodeRecord(6)
	node7 = nodeRecord(7)
	node8 = nodeRecord(8)
	node9 = nodeRecord(9)
	node10 = nodeRecord(10)
	node11 = nodeRecord(11)
	node12 = nodeRecord(12)
	node13 = nodeRecord(13)
	node14 = nodeRecord(14)
	node15 = nodeRecord(15)
	node16 = nodeRecord(16)
	node17 = nodeRecord(17)
	node18 = nodeRecord(18)
	node19 = nodeRecord(19)
	node20 = nodeRecord(20)
	node21 = nodeRecord(21)
	node22 = nodeRecord(22)
	node23 = nodeRecord(23)
	node24 = nodeRecord(24)
	node25 = nodeRecord(25)
	node26 = nodeRecord(26)
	node27 = nodeRecord(27)
	node28 = nodeRecord(28)
	node29 = nodeRecord(29)
	node30 = nodeRecord(30)
	node31 = nodeRecord(31)
	node32 = nodeRecord(32)
	node33 = nodeRecord(33)
	node34 = nodeRecord(34)
	node35 = nodeRecord(35)
	node36 = nodeRecord(36)
	node37 = nodeRecord(37)
	node38 = nodeRecord(38)
	node39 = nodeRecord(39)
	node40 = nodeRecord(40)
	node41 = nodeRecord(41)
	node42 = nodeRecord(42)
	node43 = nodeRecord(43)
	node44 = nodeRecord(44)
	node45 = nodeRecord(45)
	node46 = nodeRecord(46)
	node47 = nodeRecord(47)
	node48 = nodeRecord(48)
	node49 = nodeRecord(49)
	node50 = nodeRecord(50)
	node51 = nodeRecord(51)
	node52 = nodeRecord(52)
	node53 = nodeRecord(53)
	node54 = nodeRecord(54)
	node55 = nodeRecord(55)
	node56 = nodeRecord(56)
	node57 = nodeRecord(57)
	node58 = nodeRecord(58)
	node59 = nodeRecord(59)
	node60 = nodeRecord(60)
	
	nodes = [
		node0,
		node1,
		node2,
		node3,
		node4,
		node5,
		node6,
		node7,
		node8,
		node9,
		node10,
		node11,
		node12,
		node13,
		node14,
		node15,
		node16,
		node17,
		node18,
		node19,
		node20,
		node21,
		node22,
		node23,
		node24,
		node25,
		node26,
		node27,
		node28,
		node29,
		node30,
		node31,
		node32,
		node33,
		node34,
		node35,
		node36,
		node37,
		node38,
		node39,
		node40,
		node41,
		node42,
		node43,
		node44,
		node45,
		node46,
		node47,
		node48,
		node49,
		node50,
		node51,
		node52,
		node53,
		node54,
		node55,
		node56,
		node57,
		node58,
		node59,
		node60
		]

	# Matrix of the first map
	m = [[-1]*60 for x in xrange(60)]
	m[0][1] = 1
	m[1][0] = 1
	m[1][2] = 1 
	m[2][1] = 1
	m[2][3] = 1 
	m[3][2] = 1
	m[3][4] = 1 
	m[4][3] = 1
	m[4][5] = 1 
	m[4][5] = 1
	m[5][6] = 1 
	m[6][5] = 1
	m[6][7] = 1 
	m[7][6] = 1
	m[7][8] = 1 
	m[8][7] = 1
	m[8][9] = 1 
	m[9][8] = 1
	m[9][10] = 1 
	m[10][1] = 1
	m[10][11] = 1 
	m[11][10] = 1
	m[11][12] = 1 
	m[12][11] = 1
	m[12][13] = 1
	m[13][12] = 1
	m[14][7] = 1 
	m[7][14] = 1
	m[14][15] = 1 
	m[15][14] = 1
	m[15][16] = 1 
	m[16][15] = 1
	m[16][17] = 1 
	m[17][16] = 1
	m[18][19] = 1 
	m[19][18] = 1
	m[18][20] = 1 
	m[20][18] = 1
	m[20][21] = 1 
	m[21][20] = 1
	m[22][21] = 1 
	m[21][22] = 1
	m[23][24] = 1 
	m[24][23] = 1
	m[24][25] = 1 
	m[25][24] = 1
	m[25][26] = 1 
	m[26][25] = 1
	m[26][27] = 1 
	m[27][26] = 1
	m[27][28] = 1 
	m[28][27] = 1
	m[28][13] = 1 
	m[13][28] = 1
	m[28][29] = 1 
	m[29][28] = 1
	m[29][30] = 1 
	m[30][29] = 1
	m[30][31] = 1 
	m[31][30] = 1
	m[31][32] = 1 
	m[32][31] = 1
	m[32][33] = 1 
	m[33][32] = 1
	m[33][34] = 1 
	m[34][33] = 1
	m[34][35] = 1 
	m[35][34] = 1
	m[35][36] = 1 
	m[36][35] = 1
	m[36][37] = 1 
	m[37][36] = 1
	m[38][39] = 1 
	m[39][38] = 1
	m[39][41] = 1 
	m[41][39] = 1
	m[40][41] = 1 
	m[41][40] = 1
	m[42][43] = 1 
	m[43][42] = 1
	m[43][36] = 1 
	m[36][43] = 1
	m[43][44] = 1 
	m[44][43] = 1
	m[44][35] = 1 
	m[35][44] = 1
	m[44][45] = 1 
	m[45][44] = 1
	m[46][47] = 1 
	m[47][46] = 1
	m[31][46] = 1 
	m[46][31] = 1
	m[47][48] = 1 
	m[48][47] = 1
	m[48][49] = 1 
	m[49][48] = 1
	m[49][50] = 1 
	m[50][49] = 1
	m[50][51] = 1 
	m[51][50] = 1
	m[51][52] = 1 
	m[52][51] = 1
	m[52][53] = 1 
	m[52][53] = 1
	m[52][45] = 1 
	m[45][52] = 1
	m[53][54] = 1 
	m[54][53] = 1
	m[54][55] = 1 
	m[55][54] = 1
	m[55][42] = 1 
	m[42][55] = 1
	m[55][56] = 1 
	m[56][55] = 1
	m[57][56] = 1 
	m[56][57] = 1
	m[58][57] = 1 
	m[57][58] = 1
	m[58][59] = 1 
	m[59][58] = 1
	m[59][40] = 1 
	m[40][59] = 1

	#goal = getTriangle(ts,player.position)
	#start = getTriangle(ts,enemy.position)
	goal = node13
	start = node15
	
	graph = [ 
		[-1,2,4,-1,-1,-1,-1],
		[-1,-1,-1,3,4,-1,-1],
		[-1,-1,-1,-1,6,-1,-1],
		[-1,-1,-1,-1,-1,-1,6],
		[-1,-1,-1,-1,-1,2,-1],
		[-1,-1,-1,-1,-1,-1,3],
		[-1,-1,-1,-1,-1,-1,-1]
	] 
     	# Initialize the record for the start node
     	startRecord = nodeRecord(0)
     	startRecord.connection = None
     	startRecord.costSoFar = 0

   	startRecord.estimatedTotalCost = 0.0 #node0.estimate(node6)

   	# Initialize the openList and closed lists
   	openList = []
   	
   	openList.append(startRecord)

   	closed = []
	
   	# Iterate through processing each node

   	while len(openList) > 0:
		connections = []
		
     		# Find the smallest element in the openList list
     		# (using the estimatedTotalCost)

     		current = minNode(openList)

		#print "current = " + str(current.node)

     		# If it is the goal node, then terminate
     		if current.node == goal.node: break

     		# Otherwise get its outgoing connections
     		#connections = graph.getConnections(current)
     		for index in range(0,len(m)):
     		
     			if m[current.node][index]!=-1:
     			
     				new_connection = Connection()
				new_connection.cost = m[current.node][index]
     				new_connection.fromNode = current
     				new_connection.toNode = nodes[index] 
     				connections.append(new_connection)


     		# Loop through each connection in turn
     		for connection in connections:

       			# Get the cost estimate for the end node
       			endNode = connection.getToNode()
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

       			if i>=0:
	 			# Here we find the record in the closed list
	 			# corresponding to the endNode.
	 			endNodeRecord = closed[i]

	 			# If we didn't find a shorter route, skip
	 			if endNodeRecord.costSoFar <= endNodeCost: continue


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
			     		continue
			      	# We can use the node's old cost values
			      	# to calculate its heuristic without calling

			      	# the possibly expensive heuristic function
			 
			      	endNodeHeuristic = 0.0 #endNodeRecord. - endNodeRecord.costSoFar
			 
			 
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
			endNodeRecord.costSoFar = endNodeCost
			endNodeRecord.connection = connection
			endNodeRecord.estimatedTotalCost = endNodeCost + endNodeHeuristic
			
			try:
       				j1 = openList.index(endNode)
   			except ValueError:
       				j1 = -1
			# And add it to the openList list
		
			if j1 == -1:
	    			openList.append(endNodeRecord)
		try:
       			j2 = openList.index(current)
   		except ValueError:
       			j2 = -1
	

		# We've finished looking at the connections for
		# the current node, so add it to the closed list
		# and remove it from the openList list
		
		if j2 != -1:
			openList.remove(current)
		closed.append(current)


	####### End While Len Open !=  0

	# We're here if we've either found the goal, or
	# if we've no more nodes to search, find which.
	if current.node != goal.node:
			
		# We've run out of nodes without finding the
		# goal, so there's no solution
		return None


	else:
		# Compile the list of connections in the path
		path = []

		# Work back along the path, accumulating
		# connections

		while current != start and current.connection != None:
			path.append(current.connection)
			current = current.connection.getFromNode()

	# Reverse the path, and return it

	path.reverse()

	return path

