from structures.agents import *
from structures.bullets import *
from misc.misc import *
from misc.vector3 import *

def slow_shot(player):
	bullet = Bullet()
    	bullet.position = player.position
    	bullet.velocity = vectorPlus(vectorTimes(player.velocity,10),[10,10,10])
    	bullet.orientation = player.orientation
    	return bullet
    	#bullets = bullets + [bullet]
