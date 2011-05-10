class Align:
 
   # Holds the kinematic data for the character and target
 
   agent = Agent()
 
   target = Agent()
 
   # Holds the max angular acceleration and rotation
 
   # of the character
 
   maxAngularAcceleration = 2
 
   maxRotation = 2


   # Holds the radius for arriving at the target

   targetRadius = 5

   # Holds the radius for beginning to slow down

   slowRadius = 10


   # Holds the time over which to achieve target speed

   timeToTarget = 0.1


