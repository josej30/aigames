from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from agents import *
from kinematic import *
from kinematicSteeringOutput import *

import sys

ESCAPE = '\033'

# Tecla presionada
pressed = ""

# Number of the glut window.
window = 0

# Rotation angle for the quadrilateral.
rquadx = 0.0
rquady = 0.0

cubex = 0.0
cubez = 0.0

agent = Agent()
agent.position = [0,1,-50]
agent.velocity = [0,0,0]

agent.orientation = 10.0


target = Agent()
target.position = [0,1,50] 
target.orientation = 45.6

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):
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
def ReSizeGLScene(Width, Height):
    if Height == 0:
	    Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 300.0)
    glMatrixMode(GL_MODELVIEW)


# The main drawing function. 
def DrawGLScene():
    
    global agent, target, time, maxSpeed
   
    time = 0.01

    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()	

    # We are "undoing" the rotation so that we may rotate the quad on its own axis.
    # We also "undo" the prior translate.  This could also have been done using the
    # matrix stack.
    glLoadIdentity()
    
    # Move Right 0.0 units and into the screen 6.0 units.
    glTranslatef(0.0, -20.0, -140.0)

    # update agent's steering


 

#    steering = arrive(agent,target)
#    if steering == None:
#        print " ---> Haciendo seek!"
#        steering = seeknflee(agent,target,"seek")

    steering = face(aligne, agent, target)
    if steering == None:
        print " ---> Haciendo seek!"
        steering = arrive(agent,target)

    agent.update(steering,maxSpeed,time)


##### 12-05 12:48 ####### De aqui para arriba es lili y para abajo es pinky ##############

    #######################
    # Draw the Objects

    # Plane
    drawPlane()

    # Walls
    drawWalls(100.0,3)

    # Objective
    glPushMatrix();
    drawObjective()
    glPopMatrix();

    # Agent
    glPushMatrix();
    drawAgent()
    glPopMatrix();

    #######################

    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()


def drawWalls(tam,altura):

    glBegin(GL_QUADS);
     
    t = tam/2

    glColor3f(0.2, 0.6, 0.2);
    glVertex3f(-t, altura, -t);
    glVertex3f(t, altura, -t); 
    glVertex3f(t, 0.0, -t);    
    glVertex3f(-t, 0.0, -t);     

    glVertex3f(-t, altura, t);   
    glVertex3f(-t, altura, -t);  
    glVertex3f(-t, 0.0, -t);     
    glVertex3f(-t, 0.0, t);      

    glVertex3f(t, altura, t);    
    glVertex3f(t, altura, -t);   
    glVertex3f(t, 0.0, -t);      
    glVertex3f(t, 0.0, t);       

    glVertex3f(-t, altura, t);   
    glVertex3f(t, altura, t);    
    glVertex3f(t, 0.0, t);       
    glVertex3f(-t, 0.0, t);      

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

        glTranslatef(agent.position[0], agent.position[1], agent.position[2]);  

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

    glTranslatef(target.position[0], target.position[1], target.position[2]);

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
    	
def execute(self):

    try:
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(0, 0)
        window = glutCreateWindow("Battle Cars")
        glutDisplayFunc(DrawGLScene)
        
        glutFullScreen()
    
        glutIdleFunc(DrawGLScene)
        glutReshapeFunc(ReSizeGLScene)
        glutKeyboardFunc(keyPressed)
        InitGL(640, 480)
        glutMainLoop()
    except Exception:
        print "ERROR SAPIN@"
        sys.exit()
