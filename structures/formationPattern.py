class FormationPattern:

    	# Holds the number of slots currently in the
    	# pattern. This is updated in the getDriftOffset
    	# method. It may be a fixed value.
   	numberOfSlots = 3
 
   	# Calculates the drift offset when characters are in
   	# given set of slots
   	def getDriftOffset(slotAssignments)

   	# Gets the location of the given slot index.
   	def getSlotLocation(slotNumber)

   	# Returns true if the pattern can support the given
   	# number of slots
   	def supportsSlots(slotCount)


