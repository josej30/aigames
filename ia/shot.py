from structures.agents import *
from structures.bullets import *
from misc.misc import *
from misc.vector3 import *

def slow_shot(player, type):
	bullet = Bullet()
    	bullet.position = player.position

    	if type==1:
    		bullet.velocity = vectorPlus(vectorTimes(player.velocity,10),[5,5,5])
    	else:
    		bullet.velocity = vectorPlus(vectorTimes(player.velocity,10),[7,7,7])
    	bullet.orientation = player.orientation
    	return bullet
    	#bullets = bullets + [bullet]
