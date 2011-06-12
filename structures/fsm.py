class FSM:

    def update(self,state,life):

        fstate = "Pursue"

        # Find the correct state
        if state == 'Pursue':
            if life <= 5: 
                fstate = "Flee"
                
        elif state == 'Wander':
            if life <= 5: 
                fstate = "Flee"

        elif state == 'Astar':
            if life <= 5: 
                fstate = "Flee"

        elif state == 'Flee':
            fstate = "Flee"

        return fstate
