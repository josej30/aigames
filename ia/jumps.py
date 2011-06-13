from structures.agents import *


def scheduleJumpAction(agent):
	if agent.velocity[1] == 0:
		agent.velocity[1] = agent.maxSpeedy

       		
