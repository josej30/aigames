from structures.agents import *

distancePursue = 20

class FSM:

    def update(self,agent,characters):

        fstate = agent.state

        # Find the correct state
        if agent.state == 'Pursue':
            if agent.life <= agent.maxlife*0.25: 
                return "Flee"
            if agentNear(agent,characters,distancePursue) == None:
                return "Wander"
                
        elif agent.state == 'Wander':
            if agent.life <= agent.maxlife*0.25: 
                return "Flee"
            if agentNear(agent,characters,distancePursue) != None:
               return "Pursue"

        elif agent.state == 'Astar':
            if agent.life <= agent.maxlife*0.25: 
                return "Flee"

        elif agent.state == 'Flee':
            return "Flee"

        return fstate
