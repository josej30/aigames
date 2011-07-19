from structures.agents import *

distancePursue = 20

class FSM:

    def update(self,agent,characters,food,is_firing):

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
            if agent.life <= agent.maxlife*0.25 and len(food) <= 0:
                ret = "Flee"
            elif agent.life > agent.maxlife*0.25 and (not is_firing):
                ret = "Wander"
            elif agent.life > agent.maxlife*0.25 and is_firing:
                ret = "Astar"
            else:
                ret = "Astar"

            if agentNear(agent,characters,distancePursue) != None:
                ret = "Pursue"

            return ret

        elif agent.state == 'Flee':
            if len(food) > 0:
                return "Astar"

        return fstate
