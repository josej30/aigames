from structures.agents import *

class FSM:

    def update(self,state,life,agent,characters):

        fstate = state

        # Find the correct state
        if state == 'Pursue':
            if life <= 5: 
                return "Flee"
                
        elif state == 'Wander':
            if life <= 5: 
                return "Flee"
            near = agentNear(agent,characters,5)
            if near != None:
                #print "Pursue"
                state = "Pursue"

        elif state == 'Astar':
            if life <= 5: 
                return "Flee"

        elif state == 'Flee':
            return "Flee"

        return fstate
