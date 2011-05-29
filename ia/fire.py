def calculateFiringSolution(start, end, muzzle_v, gravity):
 
 
     	# Calculate the vector from the target back to the start
     	delta = start - end
 
     	# Calculate the real-valued a,b,c coefficients of a conventional
     	# quadratic equation
     	a = gravity * gravity
     	b = -4 * (gravity * delta + muzzle_v*muzzle_v)
     	c = 4 * delta * delta

     	# Check for no real solution
    	if 4*a*c > b*b: return None

     	# Find the candidate times
     	time0 = sqrt((-b + sqrt(b*b-4*a*c)) / (2*a))

     	time1 = sqrt((-b - sqrt(b*b-4*a*c)) / (2*a))

     	# Find the time to target
     	if times0 < 0:
     		if times1 < 0:
       		# We have no valid times
       			return None

     		else:
       			ttt = times1

   	else:
     		if times1 < 0:
       		ttt = times0
     		else:
       			ttt = min(times0, times1)


   	# Return the firing vector
   	return (2 * delta - gravity * ttt*ttt) / (2 * muzzle_v * ttt)
