
import random

class Automata1D:

    # The number of cells in our automaton
    size = 1
    # Size of a neighborhood
    NBHDSIZE = 3
    # The number of distinct states a neighborhood can be in.
    NUM_STATES = 2**NBHDSIZE
    # The number of possible rules:
    NUM_RULES = 2**NUM_STATES
    
    #lists for storing the state of the system at three differnt time steps.
    past = [];
    present = [];
    future = [];
    
    # Rule stored a an integer. This will get parsed into a lookup table
    rule = 0
    
    def __init__(self,s,r):
        self.past = [0 for i in range(0,s)]
        self.present = list(self.past)
        self.future = list(self.present)
        self.size = s
	self.rule = r%self.NUM_RULES
        self.ruleArray = self.parseRule(r)
        
    # Change the rule
    def setRule(self,r):
        self.rule = r%self.NUM_RULES
        self.ruleArray = self.parseRule(r)
    
    # Get the neighborhood of a cell as a list. Note that cell neighborhoods wrap (the first and last cells are neighbors).
    def Neighbors(self,m):
        return [(m-1)%self.size,m%self.size,(m+1)%self.size]
        
    # Given the state of a cell and it's neighbors, look up the updated state for the cell.
    def apply_rule(self,n):
        nbrs = self.Neighbors(n)
        state = 0
        for i in range(0,len(nbrs)):
            state += (2**i)*self.present[nbrs[i]]
        return self.ruleArray[state]

    # Create a lookup table based on rule
    def parseRule(self, x):
        y = x
        ret = [0 for i in range(0, self.NUM_STATES)]
        i = 0
        while(y>0):
            ret[i] = y%2
            i = i + 1
            y = y - y%2
            y = y/2
        return ret
    
    # Update the automaton by one time step.
    def step(self):
        for i in range(0,self.size):
            self.future[i] = self.apply_rule(i)
        self.past = list(self.present)
        self.present = list(self.future)
        
    # Put a living cell at index n.
    def populate(self,n):
        self.present[n%self.size] = 1
        
    # Randomly place x living cells within the automaton.
    def populateRandom(self,x):
        for i in range(0,x):
            self.populate(random.randint(0,self.size-1))
      
    # Update through t steps      
    def play(self,t):
        for i in range(0,t):
            self.step()
            print(self.present)
            print

def Main():
    return
    
if __name__ == "__main__":
    Main()
