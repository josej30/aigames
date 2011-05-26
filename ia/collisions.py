from ia.steeringBehaviours import seek
from structures.collisionDetector import *
from misc.misc import *
from misc.vector3 import *
from math import cos, sin

def collisionDetect(agent,obs):

    # Holds the minimum distance to a wall (i.e., how far
    # to avoid collision) should be greater than the
    # radius of the character.
    avoidDistance = 10.0

    # Holds the distance to look ahead for a collision
    # (i.e., the length of the collision ray)
    lookahead = 8.0

    # 1. Calculate the target to delegate to seek
        
    # Calculate the front collision ray vector
    rayVectorFront = agent.velocity
    rayVectorFront = normalize(rayVectorFront)
    rayVectorFront = addition(agent.position,vectorTimes(rayVectorFront,lookahead))

    # Calculate the right collision ray vector
    rayVectorRight = agent.velocity
    rayVectorRight = normalize(rayVectorRight)
    temp = vectorTimes(rayVectorRight,lookahead)
    temp[0] = temp[0]*cos(45)
    rayVectorRight = addition(agent.position,temp)

    # Calculate the right collision ray vector
    rayVectorLeft = agent.velocity
    rayVectorLeft = normalize(rayVectorLeft)
    temp = vectorTimes(rayVectorLeft,lookahead)
    temp[2] = temp[2]*sin(45)
    rayVectorLeft = addition(agent.position,temp)

    # Front RayVector
    glPushMatrix();
    glBegin(GL_LINES);
    glColor3f(1.0,0.0,0.0);
    glVertex3f(agent.position[0],agent.position[1],agent.position[2]);
    glVertex3f(rayVectorFront[0],rayVectorFront[1],rayVectorFront[2]);
    glEnd();
    glPopMatrix();

    # Right RayVector
    # glPushMatrix();
    # glBegin(GL_LINES);
    # glColor3f(1.0,0.0,0.0);
    # glVertex3f(agent.position[0],agent.position[1],agent.position[2]);
    # glVertex3f(rayVectorRight[0],rayVectorRight[1],rayVectorRight[2]);
    # glEnd();
    # glPopMatrix();

    # Right RayVector
    # glPushMatrix();
    # glBegin(GL_LINES);
    # glColor3f(1.0,0.0,0.0);
    # glVertex3f(agent.position[0],agent.position[1],agent.position[2]);
    # glVertex3f(rayVectorLeft[0],rayVectorLeft[1],rayVectorLeft[2]);
    # glEnd();
    # glPopMatrix();

    # Find the collision
    collision = getCollision(agent.position, rayVectorFront, obs)

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
    return CollisionPursue(seek, target, agent)
