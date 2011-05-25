class DefensiveCirclePattern:


     	# The radius of one character, this is needed to determine
     	# how close we can pack a given number of characters around
     	# a circle.
     	characterRadius

# Calculates the number of slots in the pattern from
# the assignment data. This is not part of the formation
# pattern interface.
def calculateNumberOfSlots(assignments):

       	# Find the number of filled slots: it will be the
       	# highest slot number in the assignments
       	filledSlots = 0
       	
       	for assignment in assignments:
         	if assignment.slotNumber >= maxSlotNumber:
           		filledSlots = assignment.slotNumber


       	# Add one to go from the index of the highest slot to the
       	# number of slots needed.
       	numberOfSlots = filledSlots + 1

       	return numberOfSlots

# Calculates the drift offset of the pattern.
def getDriftOffset(assignments):

     	# Store the center of mass
     	center = new Static()


     	# Now go through each assignment, and add its
     	# contribution to the center.
     	for assignment in assignments:

       		location = getSlotLocation(assignment.slotNumber)
       		center.position += location.position
       		center.orientation += location.orientation


     	# Divide through to get the drift offset.
     	numberOfAssignments = assignments.length()
     	center.position /= numberOfAssignments
     	center.orientation /= numberOfAssignments
     	
     	return center

# Calculates the position of a slot.
def getSlotLocation(slotNumber):

     	# We place the slots around a circle based on their
     	# slot number
     	angleAroundCircle = slotNumber / numberOfSlots * PI * 2

     	# The radius depends on the radius of the character,
     	# and the number of characters in the circle:
     	# we want there to be no gap between character’s shoulders.
     	radius = characterRadius / sin(PI / numberOfSlots)


     	# Create a location, and fill its components based
     	# on the angle around circle.
     	location = new Static()
     	location.position.x = radius * cos(angleAroundCircle)
     	location.position.z = radius * sin(angleAroundCircle)

     	# The characters should be facing out
     	location.orientation = angleAroundCircle

     	# Return the slot location
     	return location
     	
# Makes sure we can support the given number of slots
# In this case we support any number of slots.
def supportsSlots(slotCount):
     return true
