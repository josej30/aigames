from structures.agents import Agent
from structures.walls import Wall
from media.graphics2 import execute
import sys

#
# Main Program for Battle Cars
#

if len(sys.argv) != 2:
    print "USE: python battlecars.py num_enemies"
    sys.exit()

execute()
