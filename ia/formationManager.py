class FormationManager:
 
 
     	# Holds the assignment of a single character to a slot
     	struct SlotAssignment:
 
       	character
       	slotNumber
 
     	# Holds a list of slots assignments.
     	slotAssignments
 
     	# Holds a Static structure (i.e., position and orientation)
     	# representing the drift offset for the currently filled
     	# slots.
     	driftOffset

     	# Holds the formation pattern
     	pattern

# Updates the assignment of characters to slots
def updateSlotAssignments():

       	# A very simply assignment algorithm: we simply go through
       	# each assignment in the list and assign sequential slot
       	# numbers

     	for i in 0..slotAssignments.length():
         	slotAssignments[i].slotNumber = i


       	# Update the drift offset
       	driftOffset = pattern.getDriftOffset(slotAssignments)

# Add a new character to the first available slot. Returns
# false if no more slots are available.
def addCharacter(character):

       	# Find out how many slots we have occupied
      	occupiedSlots = slotAssignments.length()

       	# Check if the pattern supports more slots
       	if pattern.supportsSlots(occupiedSlots + 1):

         	# Add a new slot assignment
         	slotAssignment = new SlotAssignment()
     		slotAssignment.character = character
     		slotAssignments.append(slotAssignment)

     		# Update the slot assignments and return success
     		updateSlotAssignments()

     		return true

   	# Otherwise we’ve failed to add the character
   	return false

   # Removes a character from its slot.
def removeCharacter(character):

     	# Find the character’s slot
     	slot = charactersInSlots.find(character)

     	# Make sure we’ve found a valid result
     	if slot in 0..slotAssignments.length():

       	# Remove the slot
       	slotAssignments.removeElementAt(slot)

       	# Update the assignments
       	updateSlotAssignments()

# Write new slot locations to each character
def updateSlots():

     	# Find the anchor point
     	anchor = getAnchorPoint()

     	# Get the orientation of the anchor point as a matrix
     	orientationMatrix = anchor.orientation.asMatrix()

     	# Go through each character in turn
     	for i in 0..slotAssignments.length():

       	# Ask for the location of the slot relative to the
       	# anchor point. This should be a Static structure
       	relativeLoc = pattern.getSlotLocation(slotAssignments[i].slotNumber)


