from structures.BehaviorAndWeight import *
from structures.steeringOutput import *
from misc.vector3 import *
from ia.steeringBehaviours import *

pursue = BehaviorAndWeight(Pursue,0.2)

# Holds a list of BehaviorAndWeight instances.
behaviors = []

# Holds the maximum acceleration and rotation
maxAcceleration = 5
maxRotation = 10

# Returns the acceleration required.
def getSteering():

    # Create the steering structure for accumulation
    steering = new SteeringOutput()

    # Accumulate all accelerations
    for behavior in behaviors:
        steering += behavior.weight * behavior.behavior.getSteering()

    # Crop the result and return
    #steering.linear = max(steering.linear, maxAcceleration)
    #steering.angular = max(steering.angular, maxRotation)

    return steering
