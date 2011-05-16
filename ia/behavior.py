from structures.BehaviorAndWeight import *
from structures.steeringOutput import *
from misc.vector3 import *
from ia.steeringBehaviours import *
from ia.collisions import *

# Returns the acceleration required.
def getSteering(target,agent,obs):

    steeringPursue = Pursue(seek,target,agent)
    steeringObstacleAvoidance = collisionDetect(agent,obs)
    PursueWeight = 0.0
    ObstacleAvoidanceWeight = 1.0

    if (steeringObstacleAvoidance.linear == [0,0,0]):
        PursueWeight = 0.5
        ObstacleAvoidanceWeight = 0.5

    # Holds a list of BehaviorAndWeight instances.
    behaviors = [
        [steeringPursue,PursueWeight],
        [steeringObstacleAvoidance,ObstacleAvoidanceWeight]
        ]

    # Holds the maximum acceleration and rotation
    maxAcceleration = 5
    maxRotation = 10

    # Create the steering structure for accumulation
    steering = SteeringOutput()

    # Accumulate all accelerations
    for behavior in behaviors:
        temp = behavior[0].scale_steering(behavior[1])
        steering = sum_steering(steering, temp)


    # Crop the result and return
    #steering.linear = max(steering.linear, maxAcceleration)
    #steering.angular = max(steering.angular, maxRotation)

    return steering
