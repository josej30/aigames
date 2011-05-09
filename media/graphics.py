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
agent.position = [-50,1,-50]
agent.velocity = [10,0,0]

target = Agent()
target.position = [0,1,0] 

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

 

   # steering = arrive(agent,target)
#    if steering == None:
    print " ---> Haciendo seek!"
    steering = seeknflee(agent,target,"seek")
    agent.update(steering,maxSpeed,time)


    #######################
    # Draw the Objects
    drawPlane()
    drawAgent()
    #######################

    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()


def drawPlane():
	global rquadx, rquady, pressed
	
	# Draw a square (quadrilateral) rotated on the X axis
	if pressed == "a":
		rquadx = rquadx - 3.0                 # Decrease The Rotation Variable For The Quad
		pressed = ""
	if pressed == "w":
		rquady = rquady - 3.0                 # Decrease The Rotation Variable For The Quad
		pressed = ""
	if pressed == "s":
		rquady = rquady + 3.0                 # Decrease The Rotation Variable For The Quad
		pressed = ""
	if pressed == "d":
		rquadx = rquadx + 3.0                 # Decrease The Rotation Variable For The Quad
		pressed = ""

	glRotatef(rquadx, 0.0, 1.0, 0.0)      # Rotate X
	glRotatef(rquady, 1.0, 0.0, 0.0)      # Rotate Y

	glColor3f(0.3, 0.5, 1.0)            # Bluish shade
	glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
	glVertex3f(-50.0, 0.0, 50.0)          # Top Left
	glVertex3f(50.0, 0.0, 50.0)           # Top Right
	glVertex3f(50.0, 0.0, -50.0)          # Bottom Right
	glVertex3f(-50.0, 0.0, -50.0)         # Bottom Left
	glEnd()                             # We are done with the polygon

def drawAgent():
	global cubex, cubez, pressed, agent

	if pressed == "up":
		cubez = cubez - 0.5
		pressed = ""
	if pressed == "down":
		cubez = cubez + 0.5		
		pressed = ""
	if pressed == "left":
		cubex = cubex - 0.5
		pressed = ""
	if pressed == "right":
		cubex = cubex + 0.5
		pressed = ""

        glTranslatef(agent.position[0], agent.position[1], agent.position[2]);  

	glBegin(GL_QUADS);              

        glColor3f(0.0,1.0,0.0);         
        glVertex3f( 1.0, 1.0,-1.0);     
        glVertex3f(-1.0, 1.0,-1.0);     
        glVertex3f(-1.0, 1.0, 1.0);     
        glVertex3f( 1.0, 1.0, 1.0);     

        glColor3f(1.0,0.5,0.0);         
        glVertex3f( 1.0,-1.0, 1.0);     
        glVertex3f(-1.0,-1.0, 1.0);     
        glVertex3f(-1.0,-1.0,-1.0);     
        glVertex3f( 1.0,-1.0,-1.0);

        glColor3f(1.0,0.0,0.0);         
        glVertex3f( 1.0, 1.0, 1.0);     
        glVertex3f(-1.0, 1.0, 1.0);     
        glVertex3f(-1.0,-1.0, 1.0);     
        glVertex3f( 1.0,-1.0, 1.0);     

        glColor3f(1.0,1.0,0.0);               # Set The Color To Yellow
        glVertex3f( 1.0,-1.0,-1.0);             # Bottom Left Of The Quad (Back)
        glVertex3f(-1.0,-1.0,-1.0);             # Bottom Right Of The Quad (Back)
        glVertex3f(-1.0, 1.0,-1.0);             # Top Right Of The Quad (Back)
        glVertex3f( 1.0, 1.0,-1.0);             # Top Left Of The Quad (Back)

        glColor3f(0.0,0.0,1.0);                 # Set The Color To Blue
        glVertex3f(-1.0, 1.0, 1.0);             # Top Right Of The Quad (Left)
        glVertex3f(-1.0, 1.0,-1.0);             # Top Left Of The Quad (Left)
        glVertex3f(-1.0,-1.0,-1.0);             # Bottom Left Of The Quad (Left)
        glVertex3f(-1.0,-1.0, 1.0);             # Bottom Right Of The Quad (Left)

        glColor3f(1.0,0.0,1.0);                 # Set The Color To Violet
        glVertex3f( 1.0, 1.0,-1.0);             # Top Right Of The Quad (Right)
        glVertex3f( 1.0, 1.0, 1.0);             # Top Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0, 1.0);             # Bottom Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0,-1.0);             # Bottom Right Of The Quad (Right)
        glEnd();                                # Done Drawing The Quad


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    global pressed
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()
    if args[0] == '\141':
	    pressed = "a"
    if args[0] == '\167':
	    pressed = "w"
    if args[0] == '\163':
	    pressed = "s"
    if args[0] == '\144':
	    pressed = "d"
    if args[0] == '\152':
	    pressed = "left"
    if args[0] == '\151':
	    pressed = "up"
    if args[0] == '\154':
	    pressed = "right"
    if args[0] == '\153':
	    pressed = "down"
    	
def execute(self):

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Battle Cars")
    glutDisplayFunc(DrawGLScene)
    
#    glutFullScreen()
    
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()
