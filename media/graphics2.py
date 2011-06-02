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
from structures.triangle import *
from ia.steeringBehaviours import *
from ia.behavior import *
from ia.jumps import *

############### TODO ESTO DEBERIA IR EN EL MAIN ###########
############### O EN ALGUN LUGAR FUERA DE AQUI  ##########

sys_enemies = sys.argv[1]
sys_behavior = sys.argv[2]

# Debug Option activated/desactivated
debug = True

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

################
# Agents stuff #
################

enemy1 = Agent()
enemy1.position = [-40,0,-40]
enemy1.velocity = [0,0,0]
enemy1.orientation = 100.0

enemy2 = Agent()
enemy2.position = [40,0,40]
enemy2.velocity = [0,0,0]
enemy2.orientation = 100.0

enemy3 = Agent()
enemy3.position = [-40,0,40]
enemy3.velocity = [0,0,0]
enemy3.orientation = 10.0

enemy4 = Agent()
enemy4.position = [-40,0,-40]
enemy4.velocity = [0,0,0]
enemy4.orientation = 10.0

player = Agent()
player.position = [28,0,10] 
player.orientation = 0.0
player.maxSpeed = 0.5
player.maxAcceleration = 0.5

# How many enemies the user wants?
if sys_enemies == '1':
    enemies = [enemy1]
elif sys_enemies == '2':
    enemies = [enemy1,enemy2]
elif sys_enemies == '3':
    enemies = [enemy1,enemy2,enemy3]
elif sys_enemies == '4':
    enemies = [enemy1,enemy2,enemy3,enemy4]
else:
    print "The number of enemies are 1, 2, 3 or 4"
    sys.exit(-1)

players = [player]
characters = enemies + players

# Array that contains all the proyections of
# the walls and obstacles of the world with
# their respectives normal vectors
obs = []

# Array with the obstacle objects
obstacle_ob = []

# Triangles
ts = []

ts.append(Triangle((50,50),(30,30),(30,50),0)) #0
ts.append(Triangle((50,50),(30,30),(50,30),1)) #1

ts.append(Triangle((30,30),(50,30),(50,20),2)) #2
ts.append(Triangle((50,20),(30,30),(30,20),3)) #3

ts.append(Triangle((30,20),(30,0),(50,20),4)) #4
ts.append(Triangle((50,20),(50,0),(30,0),5)) #5

ts.append(Triangle((50,-20),(50,0),(30,0),6)) #6
ts.append(Triangle((50,-20),(30,-20),(30,0),7)) #7

ts.append(Triangle((50,-20),(30,-20),(30,-30),8)) #8
ts.append(Triangle((50,-30),(30,-30),(50,-20),9)) #9

ts.append(Triangle((50,-30),(30,-30),(50,-50),10)) #10
ts.append(Triangle((50,-50),(30,-50),(30,-30),11)) #11
    
ts.append(Triangle((20,-50),(30,-30),(30,-50),12)) #12
ts.append(Triangle((20,-30),(20,-50),(30,-30),13)) #13

ts.append(Triangle((30,-20),(30,0),(20,-20),14)) #14
ts.append(Triangle((20,0),(30,0),(20,-20),15)) #15

ts.append(Triangle((20,0),(30,0),(20,20),16)) #16
ts.append(Triangle((20,20),(30,20),(30,0),17)) #17

ts.append(Triangle((20,30),(30,30),(20,50),18)) #18
ts.append(Triangle((20,50),(30,50),(30,30),19)) #19

ts.append(Triangle((20,30),(0,30),(20,50),20)) #20
ts.append(Triangle((0,30),(0,50),(20,50),21)) #21

ts.append(Triangle((0,0),(0,20),(20,20),22)) #22
ts.append(Triangle((0,0),(20,0),(20,20),23)) #23

ts.append(Triangle((0,0),(20,0),(20,-20),24)) #24
ts.append(Triangle((0,0),(0,-20),(20,-20),25)) #25

ts.append(Triangle((0,-30),(0,-20),(20,-20),26)) #26
ts.append(Triangle((20,-20),(0,-30),(20,-30),27)) #27

ts.append(Triangle((20,-30),(20,-50),(0,-30),28)) #28
ts.append(Triangle((0,-30),(0,-50),(20,-50),29)) #29

ts.append(Triangle((-50,50),(-30,30),(-30,50),59)) #-1 59
ts.append(Triangle((-50,50),(-30,30),(-50,30),58)) #-2 58

ts.append(Triangle((-30,30),(-50,30),(-50,20),57)) #-3 57
ts.append(Triangle((-50,20),(-30,30),(-30,20),56)) #-4 56

ts.append(Triangle((-30,20),(-30,0),(-50,20),55)) #-5 55
ts.append(Triangle((-50,20),(-50,0),(-30,0),54)) #-6 54

ts.append(Triangle((-50,-20),(-50,0),(-30,0),53)) #-7 53
ts.append(Triangle((-50,-20),(-30,-20),(-30,0),52)) #-8 52

ts.append(Triangle((-50,-20),(-30,-20),(-30,-30),51)) #-9 51
ts.append(Triangle((-50,-30),(-30,-30),(-50,-20),50)) #-10 50

ts.append(Triangle((-50,-30),(-30,-30),(-50,-50),49)) #-11 49
ts.append(Triangle((-50,-50),(-30,-50),(-30,-30),48)) #-12 48

ts.append(Triangle((-20,-50),(-30,-30),(-30,-50),47)) #-13 47
ts.append(Triangle((-20,-30),(-20,-50),(-30,-30),46)) #-14 46

ts.append(Triangle((-30,-20),(-30,0),(-20,-20),45)) #-15 45
ts.append(Triangle((-20,0),(-30,0),(-20,-20),44)) #-16 44

ts.append(Triangle((-20,0),(-30,0),(-20,20),43)) #-17 43
ts.append(Triangle((-20,20),(-30,20),(-30,0),42)) #-18 42

ts.append(Triangle((-20,30),(-30,30),(-20,50),41)) #-19 41
ts.append(Triangle((-20,50),(-30,50),(-30,30),40)) #-20 40

ts.append(Triangle((-20,30),(0,30),(-20,50),39)) #-21 39
ts.append(Triangle((0,30),(0,50),(-20,50),38)) #-22 38

ts.append(Triangle((0,0),(0,20),(-20,20),37)) #-23 37
ts.append(Triangle((0,0),(-20,0),(-20,20),36)) #-24 36

ts.append(Triangle((0,0),(-20,0),(-20,-20),35)) #-25 35
ts.append(Triangle((0,0),(0,-20),(-20,-20),34)) #-26 34

ts.append(Triangle((0,-30),(0,-20),(-20,-20),33)) #-27 33
ts.append(Triangle((-20,-20),(0,-30),(-20,-30),32)) #-28 32

ts.append(Triangle((-20,-30),(-20,-50),(0,-30),31)) #-29 31
ts.append(Triangle((0,-30),(0,-50),(-20,-50),30)) #-30 30


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
    obs.append( { 'height': 9999999999, 'seg': i.get_proyection() , 'normal': i.normal } )

######################
# 1st Obstacle Stuff #
######################
obstacle1 = Obstacle(-25,0,-25,10,10,3,"obstacle1")
segments1 = obstacle1.segments()
normals1 = obstacle1.normals()
for i in range(0,len(segments1)):
    obs.append( { 'height': obstacle1.height , 'seg': segments1[i] , 'normal': normals1[i] } )
    obstacle_ob.append(obstacle1)

######################
# 2st Obstacle Stuff #
######################
obstacle2 = Obstacle(25,0,-25,10,10,3,"obstacle2")
segments2 = obstacle2.segments()
normals2 = obstacle2.normals()
for i in range(0,len(segments2)):
    obs.append( { 'height': obstacle2.height, 'seg': segments2[i] , 'normal': normals2[i] } )
    obstacle_ob.append(obstacle2)

######################
# 3st Obstacle Stuff #
######################
obstacle3 = Obstacle(0,0,25,60,10,3,"obstacle_big")
segments3 = obstacle3.segments()
normals3 = obstacle3.normals()
for i in range(0,len(segments3)):
    obs.append( { 'height': obstacle3.height, 'seg': segments3[i] , 'normal': normals3[i] } )
    obstacle_ob.append(obstacle3)


############### FIN DE TODO LO QUE DEBERIA IR EN EL MAIN ###########
################## O EN ALGUN LUGAR FUERA DE AQUI  #################

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


# The main drawing function
def PaintWorld():
    
    global players, limits, obs, enemies, time2, time1, time, debug, ts

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

	# Player
        for player in players:
        	# Objective
        	glPushMatrix()
        	drawAgent(player,'cyan')
        	glPopMatrix()

        # Enemies
        for enemy in enemies:
            glPushMatrix()
            drawAgent(enemy,'red')
            glPopMatrix()

        drawNavMesh(ts)

        #######################

        #getTriangle2(ts,player.position)

        #############
        # Behaviour #
        #############
    	if sys_behavior == "Wander":
            steering1 = getSteering(characters,player,enemy1,obs,ts,"Wander")
            steering2 = getSteering(characters,player,enemy2,obs,ts,"Wander")
            steering3 = getSteering(characters,player,enemy3,obs,ts,"Wander")
            steering4 = getSteering(characters,player,enemy4,obs,ts,"Wander")
    	elif sys_behavior == "Pursue":
            steering1 = getSteering(characters,player,enemy1,obs,ts,"Pursue")
            steering2 = getSteering(characters,player,enemy2,obs,ts,"Pursue")
            steering3 = getSteering(characters,player,enemy3,obs,ts,"Pursue")
            steering4 = getSteering(characters,player,enemy4,obs,ts,"Pursue")
	elif sys_behavior == "Seek":
            steering1 = getSteering(characters,player,enemy1,obs,ts,"Seek")
            steering2 = getSteering(characters,player,enemy2,obs,ts,"Seek")
            steering3 = getSteering(characters,player,enemy3,obs,ts,"Seek")
            steering4 = getSteering(characters,player,enemy4,obs,ts,"Seek")
	elif sys_behavior == "Astar":
            steering1 = getSteering(characters,player,enemy1,obs,ts,"Astar")
#            steering2 = getSteering(characters,player,enemy2,obs,ts,"Astar")
#            steering3 = getSteering(characters,player,enemy3,obs,ts,"Astar")
#            steering4 = getSteering(characters,player,enemy4,obs,ts,"Astar")
    	else:
            print "USE: python battlecars.py num_enemies [ Wander | Pursue | Seek | Astar ]"
            sys.exit()

        ###########
        # Physics #
        ###########
        ans = check_physics(characters,obs,obstacle_ob)
        
        # Get end just before calculating new positions,
        # velocities and accelerations
        time2 = datetime.now()
    
        time = ( (time2 - time1).microseconds ) / 1000000.0

        # Updating player stats
        updatePlayer(player,time)

        # Updating enemies stats
        if sys_enemies == '1':
            enemy1.update(steering1,time)
        elif sys_enemies == '2':
            enemy1.update(steering1,time)
            enemy2.update(steering2,time)
        elif sys_enemies == '3':
            enemy1.update(steering1,time)
            enemy2.update(steering2,time)
            enemy3.update(steering3,time)
        elif sys_enemies == '4':
            enemy1.update(steering1,time)
            enemy2.update(steering2,time)
            enemy3.update(steering3,time)
            enemy4.update(steering4,time)
        for col in ans:
            col[0].update(col[1],time)

        # Get initial time just after calculating everything
        time1 = datetime.now()
        
        ####################
        # End of Behaviour #
        ####################

        glutSwapBuffers()

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)

def drawNavMesh(ts):

    y = 0.1
    if not debug:
        y = -0.3

    for t in ts:
        
        glPushMatrix()
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,0.8)
        glVertex3f(t.vertex1[0],y,t.vertex1[1])
        glVertex3f(t.vertex2[0],y,t.vertex2[1])
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,0.8)
        glVertex3f(t.vertex2[0],y,t.vertex2[1])
        glVertex3f(t.vertex3[0],y,t.vertex3[1])
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,0.8)
        glVertex3f(t.vertex3[0],y,t.vertex3[1])
        glVertex3f(t.vertex1[0],y,t.vertex1[1])
        glEnd()
        glPopMatrix()

        g = t.centerOfMass()

        glPushMatrix()
        glColor3f(1.0,1.0,0.0)
        glTranslatef(g[0], y, g[1])
        glutSolidSphere(0.2,20,20)
        glPopMatrix()

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
    global keyBuffer, debug
    
    # Print NavMesh (Debug Mode)
    if ord(key) == 112:
        debug = not debug

    else:
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

    global player, keyBuffer, rquadx, rquady

    step = 0.5
    acc = player.maxAcceleration

    # Movements of the player
    if keyBuffer[100]:
        steering = SteeringOutput()
        steering.linear = [-acc,0,0]
        player.update(steering,time)
        #print "Left"
    if keyBuffer[101]:
        steering = SteeringOutput()
        steering.linear = [0,0,-acc]
        player.update(steering,time)
        #print "Up"
    if keyBuffer[102]:
        steering = SteeringOutput()
        steering.linear = [acc,0,0]
        player.update(steering,time)
        #print "Right"
    if keyBuffer[103]:
        steering = SteeringOutput()
        steering.linear = [0,0,acc]
        player.update(steering,time)
        #print "Down"
    if keyBuffer[42]:
        scheduleJumpAction(player)

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
    
    #glutFullScreen()
    
    glutIdleFunc(PaintWorld)
    glutReshapeFunc(ReSizeWorld)

    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUp)
    glutSpecialFunc(keySpecial)
    glutSpecialUpFunc(keySpecialUp)

    InitWorld(640, 480)

    glutMainLoop()
