from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from datetime import datetime
from random import random
import traceback
import sys

from misc.tactic import *
from misc.matrix import *
from misc.refreshMap import *
from misc.neighbors import *
from physics.rules import *
from structures.agents import *
from structures.walls import *
from structures.obstacles import *
from structures.steeringOutput import *
from structures.triangle import *
from structures.bullets import *
from structures.fsm import FSM
from ia.steeringBehaviours import *
from ia.behavior import *
from ia.jumps import *
from ia.shot import *

############### TODO ESTO DEBERIA IR EN EL MAIN ###########
############### O EN ALGUN LUGAR FUERA DE AQUI  ##########

sys_enemies = sys.argv[1]

# Debug Option activated/desactivated
debug = True

# Keyboard keys pressed
keyBuffer = [False for x in range(256)]

# Time Stuff
time = 0
rtime = 0
time1 = datetime.now()
time2 = datetime.now()
ftime = datetime.now()
itime = datetime.now()

# Size of the world
size = 100

# Rotation angles for the floor
rquadx = 0.0
rquady = 0.0

###############
# Bullets #####
###############

enemy_bullets = []
player_bullets = []

########
# Food #
########

food = []

################
# Agents stuff #
################

enemy1 = Agent()
enemy1.position = [40,0,-40]
enemy1.velocity = [0,0,0]
enemy1.orientation = 100.0
enemy1.color = 1

enemy2 = Agent()
enemy2.position = [40,0,40]
enemy2.velocity = [0,0,0]
enemy2.orientation = 100.0
enemy2.color = 2

enemy3 = Agent()
enemy3.position = [-40,0,40]
enemy3.velocity = [0,0,0]
enemy3.orientation = 100.0
enemy3.color = 3

enemy4 = Agent()
enemy4.position = [-40,0,-40]
enemy4.velocity = [0,0,0]
enemy4.orientation = 100.0
enemy4.color = 4

player = Agent()
player.position = [28,0,10] 
player.orientation = 777.0
player.maxSpeedy = 30.0
player.maxAccelerationy = 120.0
player.maxSpeed = 10.0
player.maxAcceleration = 15.0
player.player = True

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

# The Matrix containing the connections 
# betweens the nodes of the world
mm = MatrixMap()

# Variable that holds if there is an attack
is_firing = False

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
    
    global players, limits, obs, enemies, time2, time1, time, debug, ts, enemy_bullets, player_bullets, itime, ftime, rtime, mm, is_firing

    try:

        # Keys Pressed and saved in buffer
        keyOperations()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()	        
        glLoadIdentity()
    
        glTranslatef(0.0, -20.0, -140.0)

        #######################
        # Draw the Objects

        drawLife(players[0],enemies)

        # Plane
        drawPlane()

        # Limits of the world
        drawLimits(limits)

        # Obstacles
        drawObstacle(obstacle1)
        drawObstacle(obstacle2)
        drawObstacle(obstacle3)

        # Draw Food
        drawFood(food)

	# Player
        for player in players:
            if player.life == 0:
                print ""
                print "    GAME OVER...    "
                print ""
                print "    Thanks for playing Battle Cubes :D   "
                print ""
                sys.exit(0)
            drawAgent(player)

        #Agent's Bullets
	for bullet in player_bullets:
		drawBullet(bullet,1)
		
	#Agent' Bullets
	for bullet in enemy_bullets:
		drawBullet(bullet,2)
		
	
        # Enemies
        for enemy in enemies:
	    enemy_bullets = enemy_bullets + enemy.bullets
	    enemy.bullets = []
            if enemy.life <= 0:
                enemies.remove(enemy)    
                characters.remove(enemy)
                break
            drawEnemy(enemy)

        # Drawing the Nav Mesh & the sound
        drawNavMesh(ts,mm)        

        #######################

        # Refreshing the map connections
        ftime = datetime.now()
    	
        rtime = (ftime - itime).microseconds  
        if (rtime > 900000):
            itime = datetime.now()
            refreshMap(mm)

        go = True
        # Refreshing the is_firing status
        for i in range(len(mm.m)):
            for j in range(len(mm.m)):
                if mm.m[i][j] != -1 and mm.m[i][j]!=20:
                    go = False
        if go:
            is_firing = False

        #############
        # Behaviour #
        #############

        fsm = FSM()
        steerings = [SteeringOutput(),SteeringOutput(),SteeringOutput(),SteeringOutput()]

        tg = TacticGraph()
        
        player.life = 20

        # Iterating through all the enemies
        for i in range(0,len(enemies)):
            enemy = enemies[i]
            if enemy.life > 0:
                # Updating the state on the FSM
                enemy.state = fsm.update(enemy,characters,food,is_firing)
                # Retrieving the new steering
                steerings[i] = getSteering(characters,player,
                                           enemy,obs,ts,food,tg,mm)

        physics = check_physics(characters,obs,obstacle_ob)
        
        # Get end just before calculating new positions,
        # velocities and accelerations
        time2 = datetime.now()
    	
        time = ( (time2 - time1).microseconds ) / 1000000.0

        # Updating player stats
        updatePlayer(player,time,obstacle_ob)

	# Updating agent's bullets from agent
	for b in player_bullets:
		if b.position[1] < 0:
			player_bullets.remove(b)
		else:
			#print b.velocity
			steering = SteeringOutput()
			# Acceleration in y-axes (gravity)
			b.update(steering, time)

			#Check bullet position
			check_shot(b,enemies)
			for ob in obstacle_ob:
				if inside_ob(b,ob):
					
					player_bullets.remove(b)
					break
			#for wall in obs:
			#	agent_wall(agent,wall)
					
			#print "posicion " + str(b.position)
			
        #Updating enemy's bullets 
	for b in enemy_bullets:
		if b.position[1] < 0:
			enemy_bullets.remove(b)
		else:
			#print b.velocity
			steering = SteeringOutput()
			# Acceleration in y-axes (gravity)
			b.update(steering, time)

			#Check bullet position
			check_shot(b,[player])
			for ob in obstacle_ob:
				if inside_ob(b,ob):
					
					enemy_bullets.remove(b)
					break
       

        #print player.velocity


        # Updating enemies stats
        for i in range(0,len(enemies)):
            if enemies[i].life > 0:
                enemies[i].update(steerings[i],time,obstacle_ob,"auto")

        for col in physics:
            col[0].update(col[1],time,obstacle_ob,"auto")

        # Get initial time just after calculating everything
        time1 = datetime.now()
        
        ####################
        # End of Behaviour #
        ####################

        glutSwapBuffers()

    except Exception, e:
        traceback.print_exc()
        sys.exit(-1)

def drawBullet(bullet,color):
	b =bullet.position
	glPushMatrix()

	if color == 1:
		glColor3f(1.0,1.0,1.0)
		glTranslatef(b[0], b[1] , b[2])
		glutSolidSphere(0.5,20,20)
		glPopMatrix()
		
	else:
		glColor3f(.0,.0,.0)
		glTranslatef(b[0], b[1] , b[2])
		glutSolidSphere(0.5,20,20)
		glPopMatrix()
		
	#glTranslatef(b[0], b[1] , b[2])
	#sglutSolidSphere(0.5,20,20)
	#glPopMatrix()

def drawNavMesh(ts,mm):

    y = 0.1
    if not debug:
        y = -0.3

    diameters = [9999999 for x in xrange(60)]
    # Checking if this node is near from an audible shot
    # and representing it correctly
    for i in range(len(mm.m)):
        for j in range(len(mm.m)):
            if mm.m[i][j] < diameters[j] and mm.m[i][j]!=-1:
                diameters[j] = (mm.m[i][j]-20)/20.0
                if diameters[j] == 10:
                    diameters[j] = 0

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
        glutSolidSphere(diameters[t.node],20,20)
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

def drawLife(player,enemies):

    x = -45.0
    y = 55.0

    bar_len = 10

    glColor3f(0.9,0.9,0.9);
    glBegin(GL_QUADS)                 
    glVertex3f(x, y+0.5, 50.0)      
    glVertex3f(x+bar_len, y+0.5, 50.0)       
    glVertex3f(x+bar_len, y, 50.0)      
    glVertex3f(x, y, 50.0)      
    glEnd()     

    life_size = (bar_len*1.0)/(player.maxlife*1.0)
    fringe = max(0,(life_size*player.life))

    # Player Life
    glColor3f(0.0, 1.0, 0.0)           
    glBegin(GL_QUADS)                 
    glVertex3f(x, y, 50.0)      
    glVertex3f(x+fringe, y, 50.0)       
    glVertex3f(x+fringe, y-2, 50.0)      
    glVertex3f(x, y-2, 50.0)      
    glEnd()     

    glColor3f(1.0, 0.0, 0.0)           
    glBegin(GL_QUADS)                 
    glVertex3f(x+fringe, y, 50.0)      
    glVertex3f(x+bar_len, y, 50.0)       
    glVertex3f(x+bar_len, y-2, 50.0)      
    glVertex3f(x+fringe, y-2, 50.0) 
    glEnd()     

    x = x+15

    # Enemies Lifes
    for enemy in enemies:

        # Enemy color
        if enemy.color == 1:
            glColor3f(0.9,0.9,0.0);
        elif enemy.color == 2:
            glColor3f(0.9,0.0,0.9);
        elif enemy.color == 3:
            glColor3f(0.0,0.0,0.9);
        elif enemy.color == 4:
            glColor3f(0.0,0.9,0.9);
        glBegin(GL_QUADS)                 
        glVertex3f(x, y+0.5, 50.0)      
        glVertex3f(x+bar_len, y+0.5, 50.0)       
        glVertex3f(x+bar_len, y, 50.0)      
        glVertex3f(x, y, 50.0)      
        glEnd()     

        life_size = (bar_len*1.0)/(enemy.maxlife*1.0)
        fringe = max(0,(life_size*enemy.life))

        # Enemy Life
        glColor3f(0.0, 1.0, 0.0)           
        glBegin(GL_QUADS)                 
        glVertex3f(x, y, 50.0)      
        glVertex3f(x+fringe, y, 50.0)       
        glVertex3f(x+fringe, y-2, 50.0)      
        glVertex3f(x, y-2, 50.0)      
        glEnd()     
        
        glColor3f(1.0, 0.0, 0.0)           
        glBegin(GL_QUADS)                 
        glVertex3f(x+fringe, y, 50.0)      
        glVertex3f(x+bar_len, y, 50.0)       
        glVertex3f(x+bar_len, y-2, 50.0)      
        glVertex3f(x+fringe, y-2, 50.0) 
        glEnd()     
        
        x = x+15

    
def drawAgent(agent):

    glPushMatrix()

    glTranslatef(agent.position[0], agent.position[1]+1, agent.position[2]);

    glBegin(GL_QUADS);              

    glColor3f(0.8,0.8,0.8);
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

    glColor3f(0.6,0.6,0.6);
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

    glPopMatrix()            

def drawEnemy(enemy):

    glPushMatrix()

    glTranslatef(enemy.position[0], enemy.position[1]+1, enemy.position[2]);

    # Yellow
    if enemy.color == 1:
        glColor3f(0.8,0.8,0.0);
    elif enemy.color == 2:
        glColor3f(0.8,0.0,0.8);
    elif enemy.color == 3:
        glColor3f(0.0,0.0,0.8);
    elif enemy.color == 4:
        glColor3f(0.0,0.7,0.7);

    if enemy.life <= enemy.maxlife*0.25:
        glColor3f(0.7,0.0,0.0);

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
    
    # Yellow
    if enemy.color == 1:
        glColor3f(0.5,0.5,0.0);
    elif enemy.color == 2:
        glColor3f(0.5,0.0,0.5);
    elif enemy.color == 3:
        glColor3f(0.0,0.0,0.5);
    elif enemy.color == 4:
        glColor3f(0.0,0.4,0.4);

    if enemy.life <= enemy.maxlife*0.25:
        glColor3f(0.5,0.0,0.0);

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

    glPopMatrix()            

def createFood(food):
    
    global ts

    r = 1.0    
    while r > 0.6:
        r = random()
    r = int(r*100)
    t = None
    for i in ts:
        if r == i.node:
            t = i
            break
    
    food.append(t)

def drawFood(food):

    global characters

    # Check if someone is eating and recovering its life
    check_food(food,characters)

    for f in food:
        pos = f.centerOfMass()

        # Drawing the food
        glPushMatrix()
        glColor3f(0.8,0.2,0.0)
        glTranslatef(pos[0], 1 , pos[1])
        glutSolidSphere(1.0,20,20)
        glPopMatrix()
        
# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(key, x , y):
    global keyBuffer, debug, enemy1, enemy2, enemy3, enemy4, player, player_bullets, enemies, is_firing
    
    # Print NavMesh (Debug Mode)
    if ord(key) == 112:
        debug = not debug
    # Enemy1 is damaged
    elif ord(key) == 49:
        enemy1.life = enemy1.life - 1
    # Enemy2 is damaged
    elif ord(key) == 50:
        enemy2.life = enemy2.life - 1
    # Enemy3 is damaged
    elif ord(key) == 51:
        enemy3.life = enemy3.life - 1
    # Enemy4 is damaged
    elif ord(key) == 52:
        enemy4.life = enemy4.life - 1
    # Create food
    elif ord(key) == 110:
        createFood(food)
    elif ord(key) == 98:
    	#print "crear bala"
    	#bullet = Bullet()
    	#bullet.position = player.position
    	#bullet.velocity = vectorPlus(vectorTimes(player.velocity,10),[10,10,10])
    	#bullet.orientation = player.orientation
        for e in enemies:
            e.state = "Astar"
        is_firing = True
        neighbors(getTriangle(ts,player.position).node,mm)
    	player_bullets = player_bullets + [slow_shot(player,2)]
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
        player.update(steering,time,obstacle_ob,"manual")
        player.orientation = getNewOrientation(player.orientation,player.velocity)
        #print "Left"
    if keyBuffer[101]:
        steering = SteeringOutput()
        steering.linear = [0,0,-acc]
        player.update(steering,time,obstacle_ob,"manual")
        player.orientation = getNewOrientation(player.orientation,player.velocity)
        #print "Up"
    if keyBuffer[102]:
        steering = SteeringOutput()
        steering.linear = [acc,0,0]
        player.update(steering,time,obstacle_ob,"manual")
        player.orientation = getNewOrientation(player.orientation,player.velocity)
        #print "Right"
    if keyBuffer[103]:
        steering = SteeringOutput()
        steering.linear = [0,0,acc]
        player.update(steering,time,obstacle_ob,"manual")
        player.orientation = getNewOrientation(player.orientation,player.velocity)
        #print "Down"
    if keyBuffer[42]:
        scheduleJumpAction(player)
        keyBuffer[42] = False

        
    # Movements of the world
    if keyBuffer[107]:
        #print "a"
        rquadx = rquadx - step
    if keyBuffer[129]:
        #print "w"
        rquady = rquady - step
    if keyBuffer[125]:
        #print "s"
        rquady = rquady + step  
    if keyBuffer[110]:
        #print "d"
        rquadx = rquadx + step
    # Quitting the game
    if keyBuffer[37]:
        sys.exit()

def execute():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(400, 100)
    window = glutCreateWindow("Battle Cubes")

    glutDisplayFunc(PaintWorld)
    
#    glutFullScreen()

    glutIdleFunc(PaintWorld)
    glutReshapeFunc(ReSizeWorld)

    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUp)
    glutSpecialFunc(keySpecial)
    glutSpecialUpFunc(keySpecialUp)

    InitWorld(640, 480)

    glutMainLoop()
