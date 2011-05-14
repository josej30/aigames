from ia.steeringBehaviours import seeknflee
from structures.collisionDetector import *
from misc.misc import *
from misc.vector3 import *

def collisionDetect(agent,obs):

    # Holds the minimum distance to a wall (i.e., how far
    # to avoid collision) should be greater than the
    # radius of the character.
    avoidDistance = 15

    # Holds the distance to look ahead for a collision
    # (i.e., the length of the collision ray)
    lookahead = 30

    # 1. Calculate the target to delegate to seek
        
    # Calculate the collision ray vector
    rayVector = agent.position
    rayVector = normalize(rayVector)
    rayVector = vectorTimes(rayVector,lookahead)

    glPushMatrix();
    glBegin(GL_LINES);
    glColor3f(1.0,0.0,0.0);
    glVertex3f(agent.position[0],agent.position[1],agent.position[2]);
    glVertex3f(rayVector[0],rayVector[1],rayVector[2]);
    glEnd();
    glPopMatrix();

    # Find the collision
    collision = getCollision(agent.position, rayVector, obs)

    # If have no collision, do nothing
    if collision == None:
        return None

    # Otherwise create a target
    target = Agent()
    target.position = addition(collision.position,collision.normal)
    target.position = vectorTimes(target.position,avoidDistance)

    # 2. Delegate to seek
    return seeknflee(agent,target,"seek")
