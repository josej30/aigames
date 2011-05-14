from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from agents import *
from walls import *

from structures.agents import *
from structures.walls import *
from ia.steeringBehaviours import *
from ia.collisions import *
from ia.jumps import *


import traceback

import sys

############### TODO ESTO DEBERIA IR EN EL MAIN ###########
############### O EN ALGUN LUGAR FUERA DE AQUI  ##########

# Size of the world
size = 100

# Rotation angles for the floor
rquadx = 0.0
rquady = 0.0


###############
# Agent stuff #
###############
agent = Agent()
agent.position = [0,0,40]

agent.velocity = [3,0,0]


agent.orientation = 100.0


################
# Target Stuff #
################
target = Agent()
target.position = [-10,0,-10] 
target.orientation = 300.0


####################
# 2nd Target Stuff #
####################
target2 = Agent()
target2.position = [0,0,0] 
target2.orientation = 0.0


# Array that contains all the proyections of
# the walls and obstacles of the world
obs = []

# Walls representing the limits of the world
c = size/2
limits = [
    Wall(-c,-c,-c,c,3),
    Wall(-c,-c,c,-c,3),
    Wall(c,c,-c,c,3),
    Wall(c,c,c,-c,3)
    ]
# Inserting every wall into the world
for i in limits:
    obs.append(i.get_proyection())

############### FIN DE TODO LO QUE DEBERIA IR EN EL MAIN ###########
################## O EN ALGUN LUGAR FUERA DE AQUI  #################

# Escape key code
ESCAPE = '\033'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitWorld(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)		
    glDepthFunc(GL_LESS)	
    glEnable(GL_DEPTH_TEST)	
    glShadeModel(GL_SMOOTH)	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()	
    
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeWorld(Width, Height):
    if Height == 0:
	    Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 300.0)
    glMatrixMode(GL_MODELVIEW)


# The main drawing function. 
def PaintWorld():
    
    global agent, target, time, maxSpeed, limits, obs
   
    try:

        time = 0.01
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()	        
        glLoadIdentity()
    
        glTranslatef(0.0, -20.0, -140.0)


        #    steering = arrive(agent,target)
        #    if steering == None:
        #        print " ---> Haciendo seek!"
        #        steering = seeknflee(agent,target,"seek")


        #steering = Pursue(seeknflee,target, agent)
        #if steering == None:
         #   print " ---> Haciendo seek!"
         #  steering = arrive(agent,target)


        steering = Pursue(seeknflee,target, agent)
        pepe = collisionDetect(agent,obs)
        if steering == None:
            print " ---> Haciendo seek!"
            steering = arrive(agent,target)
        agent.update(steering,maxSpeed,time)

       

    	#steering = Jump(agent)
    	#if steering == None:
        #	print " ---> Haciendo seek!"
        #	steering = arrive(agent,target)
    	#agent.update(steering,maxSpeed,time)

       

#    	steering = wander(face,agent,target)
#    	if steering == None:
#        	print " ---> Haciendo seek!"
#        	steering = arrive(agent,target)
#    	agent.update(steering,maxSpeed,time)
  
        ##### 12-05 12:48 ####### De aqui para arriba es lili y para abajo es pinky ##############


        #######################
        # Draw the Objects

        # Plane
        drawPlane()

        # Limits of the world
        drawLimits(limits)

        # Objective
        glPushMatrix();
        drawObjective()
        glPopMatrix();

        # Agent
        glPushMatrix();
        drawAgent()
        glPopMatrix();

        #######################

        glutSwapBuffers()
    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)


def drawLimits(limits):

    glBegin(GL_QUADS);
     
    glColor3f(0.2, 0.6, 0.2);
    glVertex3f(limits[0].x1, limits[0].height, limits[0].z1);
    glVertex3f(limits[0].x2, limits[0].height, limits[0].z2);
    glVertex3f(limits[0].x2, 0.0, limits[0].z2);
    glVertex3f(limits[0].x1, 0.0, limits[0].z1);

    glVertex3f(limits[1].x1, limits[1].height, limits[1].z1);
    glVertex3f(limits[1].x2, limits[1].height, limits[1].z2);
    glVertex3f(limits[1].x2, 0.0, limits[1].z2);
    glVertex3f(limits[1].x1, 0.0, limits[1].z1);

    glVertex3f(limits[2].x1, limits[2].height, limits[2].z1);
    glVertex3f(limits[2].x2, limits[2].height, limits[2].z2);
    glVertex3f(limits[2].x2, 0.0, limits[2].z2);
    glVertex3f(limits[2].x1, 0.0, limits[2].z1);

    glVertex3f(limits[3].x1, limits[3].height, limits[3].z1);
    glVertex3f(limits[3].x2, limits[3].height, limits[3].z2);
    glVertex3f(limits[3].x2, 0.0, limits[3].z2);
    glVertex3f(limits[3].x1, 0.0, limits[3].z1);

    glEnd();       

def drawPlane():

	global rquadx, rquady

	glRotatef(rquadx, 0.0, 1.0, 0.0)  
	glRotatef(rquady, 1.0, 0.0, 0.0)  

	glColor3f(0.5, 0.5, 0.5)           
	glBegin(GL_QUADS)                  
	glVertex3f(-50.0, 0.0, 50.0)      
	glVertex3f(50.0, 0.0, 50.0)       
	glVertex3f(50.0, 0.0, -50.0)      
	glVertex3f(-50.0, 0.0, -50.0)     
	glEnd()                           

def drawAgent():

	global agent

        glTranslatef(agent.position[0], agent.position[1]+1, agent.position[2]);  

	glBegin(GL_QUADS);              

        glColor3f(0.0,0.0,0.8);         
        glVertex3f( 1.0, 1.0,-1.0);     
        glVertex3f(-1.0, 1.0,-1.0);     
        glVertex3f(-1.0, 1.0, 1.0);     
        glVertex3f( 1.0, 1.0, 1.0);     

        glColor3f(0.0,0.0,0.8);         
        glVertex3f( 1.0,-1.0, 1.0);     
        glVertex3f(-1.0,-1.0, 1.0);     
        glVertex3f(-1.0,-1.0,-1.0);     
        glVertex3f( 1.0,-1.0,-1.0);

        glColor3f(0.0,0.0,0.8);         
        glVertex3f( 1.0, 1.0, 1.0);     
        glVertex3f(-1.0, 1.0, 1.0);     
        glVertex3f(-1.0,-1.0, 1.0);     
        glVertex3f( 1.0,-1.0, 1.0);     

        glColor3f(0.0,0.0,0.5);    
        glVertex3f( 1.0,-1.0,-1.0);
        glVertex3f(-1.0,-1.0,-1.0);
        glVertex3f(-1.0, 1.0,-1.0);
        glVertex3f( 1.0, 1.0,-1.0);

        glColor3f(0.0,0.0,0.5);    
        glVertex3f(-1.0, 1.0, 1.0);
        glVertex3f(-1.0, 1.0,-1.0);
        glVertex3f(-1.0,-1.0,-1.0);
        glVertex3f(-1.0,-1.0, 1.0);

        glColor3f(0.0,0.0,0.5);    
        glVertex3f( 1.0, 1.0,-1.0);
        glVertex3f( 1.0, 1.0, 1.0);
        glVertex3f( 1.0,-1.0, 1.0);
        glVertex3f( 1.0,-1.0,-1.0);
        glEnd();

def drawObjective():
    
    global target

    glTranslatef(target.position[0], target.position[1]+1, target.position[2]);

    glBegin(GL_TRIANGLES);

    glColor3f(0.9,0.0,0.0);
    glVertex3f( 0.0, 1.0, 0.0);
    glVertex3f(-1.0,-1.0, 1.0);
    glVertex3f( 1.0,-1.0, 1.0);

    glColor3f(0.6,0.0,0.0);	
    glVertex3f( 0.0, 1.0, 0.0);
    glVertex3f( 1.0,-1.0, 1.0);
    glVertex3f( 1.0,-1.0, -1.0);
		
    glColor3f(0.9,0.0,0.0);	
    glVertex3f( 0.0, 1.0, 0.0);
    glVertex3f( 1.0,-1.0, -1.0);
    glVertex3f(-1.0,-1.0, -1.0);
		
    glColor3f(0.6,0.0,0.0);
    glVertex3f( 0.0, 1.0, 0.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(-1.0,-1.0, 1.0);
    glEnd();			


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):

    global target, rquadx, rquady

    # Step (rate) to move the target
    # Increase this and the target will move faster
    step_t = 0.5

    # Step (rate) to rotate the plane
    # Increase this and the plane will rotate faster
    step_p = 3.0

    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()
    if args[0] == '\141':
        rquadx = rquadx - step_p
    if args[0] == '\167':
        rquady = rquady - step_p
    if args[0] == '\163':
        rquady = rquady + step_p   
    if args[0] == '\144':
        rquadx = rquadx + step_p   
    if args[0] == '\152':
        target.position[0] = target.position[0] - step_t
    if args[0] == '\151':
        target.position[2] = target.position[2] - step_t
    if args[0] == '\154':
        target.position[0] = target.position[0] + step_t
    if args[0] == '\153':
        target.position[2] = target.position[2] + step_t
    	
def execute():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Battle Cars")
    glutDisplayFunc(PaintWorld)
    
    #        glutFullScreen()
    
    glutIdleFunc(PaintWorld)
    glutReshapeFunc(ReSizeWorld)
    glutKeyboardFunc(keyPressed)
    InitWorld(640, 480)
    glutMainLoop()
