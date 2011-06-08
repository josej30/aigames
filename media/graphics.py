from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from datetime import datetime
import traceback
import sys

from physics.rules import *
from structures.agents import *
from structures.walls import *
from structures.obstacles import *
from structures.steeringOutput import *
from structures.triangle import Triangle
from ia.steeringBehaviours import *
from ia.behavior2 import *
from ia.jumps import *

############### TODO ESTO DEBERIA IR EN EL MAIN ###########
############### O EN ALGUN LUGAR FUERA DE AQUI  ##########

# Keyboard keys pressed
keyBuffer = [False for x in range(256)]

# Time Stuff
time = 0
time1 = datetime.now()
time2 = datetime.now()

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
agent.velocity = [0,0,0]
agent.orientation = 100.0

###############
# Agent2 stuff #
###############
agent2 = Agent()
agent2.position = [40,0,0]
agent2.velocity = [0,0,0]
agent2.orientation = 100.0

###############
# Agent3 stuff #
###############
agent3 = Agent()
agent3.position = [10,0,10]
agent3.velocity = [0,0,0]
agent3.orientation = 10.0

###############
# Agent3 stuff #
###############
agent4 = Agent()
agent4.position = [10,0,40]
agent4.velocity = [0,0,0]
agent4.orientation = 10.0


################
# Target Stuff #
################
target = Agent()
target.position = [-10,0,-10] 
target.orientation = 300.0
target.maxSpeed = 3
target.maxAcceleration = 1

####################
# 2nd Target Stuff #
####################
target2 = Agent()
target2.position = [0,0,0] 
target2.orientation = 0.0
target2.maxSpeed = 3
target2.maxAcceleration = 1

####################
# 3nd Target Stuff #
####################
target3 = Agent()
target3.position = [0,0,0] 
target3.orientation = 0.0

# List of Agents
agents = [agent,agent2,agent3, agent4]

####################
# Targets Array    #
####################

targets = [target,target2]
characters = agents + targets


# Array that contains all the proyections of
# the walls and obstacles of the world with
# their respectives normal vectors
obs = []

# Walls representing the limits of the world
c = size/2
limits = [
    Wall(-c,-c,-c,c,3,[1,0,0]),
    Wall(-c,-c,c,-c,3,[0,0,1]),
    Wall(c,c,-c,c,3,[0,0,-1]),
    Wall(c,c,c,-c,3,[-1,0,0])
    ]

# Inserting every wall into the world
for i in limits:
    obs.append( { 'seg': i.get_proyection() , 'normal': i.normal } )

######################
# 1st Obstacle Stuff #
######################
obstacle1 = Obstacle(-25,0,-25,10,10,3)
segments1 = obstacle1.segments()
normals1 = obstacle1.normals()
for i in range(0,len(segments1)):
    obs.append( { 'seg': segments1[i] , 'normal': normals1[i] } )

######################
# 2st Obstacle Stuff #
######################
obstacle2 = Obstacle(25,0,-25,10,10,3)
segments2 = obstacle2.segments()
normals2 = obstacle2.normals()
for i in range(0,len(segments2)):
    obs.append( { 'seg': segments2[i] , 'normal': normals2[i] } )

######################
# 3st Obstacle Stuff #
######################
obstacle3 = Obstacle(0,0,25,60,10,3)
segments3 = obstacle3.segments()
normals3 = obstacle3.normals()
for i in range(0,len(segments3)):
    obs.append( { 'seg': segments3[i] , 'normal': normals3[i] } )


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
    

    global agent, agent2,agent3,agent4, target, maxSpeed, limits, obs, obstacle1, time2, time1, time, agents, targets


    try:

        # Keys Pressed and saved in buffer
        keyOperations()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()	        
        glLoadIdentity()
    
        glTranslatef(0.0, -20.0, -140.0)


        #######################
        # Draw the Objects

        # Plane
        drawPlane()

        # Limits of the world
        drawLimits(limits)

        # Obstacles
        drawObstacle(obstacle1)
        drawObstacle(obstacle2)
        drawObstacle(obstacle3)

	# Objective
        for target in targets:
        	# Objective
        	glPushMatrix()
        	drawAgent(target,'cyan')
        	glPopMatrix()

        
        #for agen in agents:
        #	# Objective
        #	glPushMatrix()
        #	drawAgent(agen,'blue')
        #	glPopMatrix()

	glPushMatrix()
	drawAgent(agents[0],'red')
	glPopMatrix()

	glPushMatrix()
	drawAgent(agents[1],'blue')
	glPopMatrix()

	glPushMatrix()
	drawAgent(agents[2],'blue')
	glPopMatrix()

	glPushMatrix()
	drawAgent(agents[3],'blue')
	glPopMatrix()

        #######################


        #############
        # Behaviour #
        #############
    	if len(sys.argv) == 1:
    		print "No se recibieron argumentos"
    		sys.exit()
    	if sys.argv[1] == "Wander":
    		steering = getSteering(characters,target3,agent,obs,[],"Wander")
    		steering2 = getSteering(characters,target,agent2,obs,[],"Wander")
    		steering3 = getSteering(characters,target,agent3,obs,[],"Wander")
    		steering4 = getSteering(characters,target,agent4,obs,[],"Wander")
    	elif sys.argv[1] == "Pursue":
    		steering = getSteering(characters,target,agent,obs,[],"Pursue")
    		steering2 = getSteering(characters,target,agent2,obs,[],"Pursue")
    		steering3 = getSteering(characters,target,agent3,obs,[],"Pursue")
    		steering4 = getSteering(characters,target,agent4,obs,[],"Pursue")
	elif sys.argv[1] == "Seek":
            	steering = getSteering(characters,target,agent,obs,[],"Seek")
            	steering2 = getSteering(characters,target,agent2,obs,[],"Seek")
            	steering3 = getSteering(characters,target,agent3,obs,[],"Seek")
            	steering4 = getSteering(characters,target,agent4,obs,[],"Seek")
    	elif sys.argv[1] == "Flee":
            steering = seek(agent, target, "flee")
    	else:
    		print "Argumento invalido"
    		sys.exit()

        ###########
        # Physics #
        ###########
        ans = check_physics(characters,obs)

        # Get end just before calculating new positions,
        # velocities and accelerations
        time2 = datetime.now()
    
        time = ( (time2 - time1).microseconds ) / 1000000.0

        # Updating agents stats
        agent.update(steering,time)
        agent2.update(steering2,time)
        agent3.update(steering3,time)
        agent4.update(steering4,time)

        # Updating player stats
        updatePlayer(target,time)

        # Get initial time just after calculating everything
        time1 = datetime.now()
        
        ####################
        # End of Behaviour #
        ####################

        glutSwapBuffers()

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)

def drawObstacle(obstacle):

    x = obstacle.x
    y = obstacle.y
    z = obstacle.z
    widex = obstacle.widex/2
    widez = obstacle.widez/2
    height = obstacle.height

    glBegin(GL_QUADS);

    glColor3f(0.2, 0.5, 0.2);
    glVertex3f(x-widex,height,z-widez);
    glVertex3f(x-widex,height,z+widez);
    glVertex3f(x-widex,0,z+widez);
    glVertex3f(x-widex,0,z-widez);
    
    glVertex3f(x-widex,height,z+widez);
    glVertex3f(x+widex,height,z+widez);
    glVertex3f(x+widex,0,z+widez);
    glVertex3f(x-widex,0,z+widez);

    glVertex3f(x+widex,height,z+widez);
    glVertex3f(x+widex,height,z-widez);
    glVertex3f(x+widex,0,z-widez);
    glVertex3f(x+widex,0,z+widez);

    glVertex3f(x+widex,height,z-widez);
    glVertex3f(x-widex,height,z-widez);
    glVertex3f(x-widex,0,z-widez);
    glVertex3f(x+widex,0,z-widez);

    # Roof
    glColor3f(0.2, 0.6, 0.2);
    glVertex3f(x-widex,height,z+widez);
    glVertex3f(x+widex,height,z+widez);
    glVertex3f(x+widex,height,z-widez);
    glVertex3f(x-widex,height,z-widez);

    glEnd();

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
    
def drawAgent(agent, color):

    glTranslatef(agent.position[0], agent.position[1]+1, agent.position[2]);

    if color == 'blue':
        glColor3f(0.0,0.0,0.8);
    elif color == 'red':
        glColor3f(0.7,0.0,0.0);
    elif color == 'cyan':
        glColor3f(0.0,0.7,0.7);
    elif color == 'yellow':
        glColor3f(0.8,0.8,0.0);
    elif color == 'purple':
        glColor3f(0.8,0.0,0.8);

    glBegin(GL_QUADS);              

    glVertex3f( 1.0, 1.0,-1.0);     
    glVertex3f(-1.0, 1.0,-1.0);     
    glVertex3f(-1.0, 1.0, 1.0);     
    glVertex3f( 1.0, 1.0, 1.0);     
    
    glVertex3f( 1.0,-1.0, 1.0);     
    glVertex3f(-1.0,-1.0, 1.0);     
    glVertex3f(-1.0,-1.0,-1.0);     
    glVertex3f( 1.0,-1.0,-1.0);
    
    glVertex3f( 1.0, 1.0, 1.0);     
    glVertex3f(-1.0, 1.0, 1.0);     
    glVertex3f(-1.0,-1.0, 1.0);     
    glVertex3f( 1.0,-1.0, 1.0);     
    
    if color == 'blue':
        glColor3f(0.0,0.0,0.5);
    elif color == 'red':
        glColor3f(0.5,0.0,0.0);
    elif color == 'cyan':
        glColor3f(0.0,0.4,0.4);
    elif color == 'yellow':
        glColor3f(0.5,0.5,0.0);
    elif color == 'purple':
        glColor3f(0.5,0.0,0.5);

    glVertex3f( 1.0,-1.0,-1.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(-1.0, 1.0,-1.0);
    glVertex3f( 1.0, 1.0,-1.0);
    
    glVertex3f(-1.0, 1.0, 1.0);
    glVertex3f(-1.0, 1.0,-1.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(-1.0,-1.0, 1.0);
    
    glVertex3f( 1.0, 1.0,-1.0);
    glVertex3f( 1.0, 1.0, 1.0);
    glVertex3f( 1.0,-1.0, 1.0);
    glVertex3f( 1.0,-1.0,-1.0);

    glEnd();


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(key, x , y):
    global keyBuffer
    keyBuffer[ord(key)+10] = True

def keyUp(key, x, y):
    global keyBuffer
    keyBuffer[ord(key)+10] = False

def keySpecial(key, x, y):
    global keyBuffer
    keyBuffer[key] = True

def keySpecialUp(key, x, y):
    global keyBuffer
    keyBuffer[key] = False
    
def keyOperations():

    global target, keyBuffer, rquadx, rquady

    step = 0.5
    acc = target.maxAcceleration

    steering = SteeringOutput()

    # Movements of the player
    if keyBuffer[100]:
        steering.linear = [-acc,-10,0]
        target.update(steering,time)
        #print "Left"
    if keyBuffer[101]:
        steering.linear = [0,-10,-acc]
        target.update(steering,time)
        #print "Up"
    if keyBuffer[102]:
        steering.linear = [acc,-10,0]
        target.update(steering,time)
        #print "Right"
    if keyBuffer[103]:
        steering.linear = [0,-10,acc]
        target.update(steering,time)
        #print "Down"
    if keyBuffer[42]:
        scheduleJumpAction(target)

    # Movements of the world
    if keyBuffer[107]:
        rquadx = rquadx - step
    if keyBuffer[129]:
        rquady = rquady - step
    if keyBuffer[125]:
        rquady = rquady + step   
    if keyBuffer[110]:
        rquadx = rquadx + step

    # Quitting the game
    if keyBuffer[37]:
        sys.exit()

def execute():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Battle Cars")

    glutDisplayFunc(PaintWorld)
    
    glutFullScreen()
    
    glutIdleFunc(PaintWorld)
    glutReshapeFunc(ReSizeWorld)

    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUp)
    glutSpecialFunc(keySpecial)
    glutSpecialUpFunc(keySpecialUp)

    InitWorld(640, 480)

    glutMainLoop()
