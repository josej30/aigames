from ia.steeringBehaviours import seek
from structures.collisionDetector import *
from misc.misc import *
from misc.vector3 import *

def collisionDetect(agent,obs):

    # Holds the minimum distance to a wall (i.e., how far
    # to avoid collision) should be greater than the
    # radius of the character.
    avoidDistance = 4

    # Holds the distance to look ahead for a collision
    # (i.e., the length of the collision ray)
    lookahead = 8.0

    # 1. Calculate the target to delegate to seek
        
    # Calculate the collision ray vector
    rayVector = agent.velocity
    rayVector = normalize(rayVector)
    rayVector = addition(agent.position,vectorTimes(rayVector,lookahead)) 
#    rayVector = vectorTimes(rayVector,lookahead)
#    rayVector[1] = 0

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
        return SteeringOutput()

    # Otherwise create a target
    target = Agent()
    normal = vectorTimes(collision.normal, avoidDistance)
    target.position = addition(collision.position, normal)

    glPushMatrix()
    glColor3f(1.0,1.0,0.0)
    glTranslatef(target.position[0], 2.0, target.position[2])
    glutSolidSphere(0.5,20,20)
    glPopMatrix()

    # 2. Delegate to seek
    return seek(agent, target, "collision")
