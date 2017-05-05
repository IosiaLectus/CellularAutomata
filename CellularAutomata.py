
import random

class Automata1D:

    def __init__(self,s,r,cs=2):
        # Number of states of a single cell
        self.cell_states = cs
        # Size of a neighborhood
        self.nbhd_size = 3
        # The number of distinct states a neighborhood can be in.
        self.num_states = self.cell_states**self.nbhd_size
        # The number of possible rules:
        self.max_rule = self.cell_states**self.num_states
        #lists for storing the state of the system at three differnt time steps.
        self.past = [0 for i in range(0,s)]
        self.present = list(self.past)
        self.future = list(self.present)
        # The number of cells in our automaton
        self.size = s
        # Rule stored a an integer. This will get parsed into a lookup table
	self.rule = r%self.max_rule
        # The rule transformed into a lookup table
        self.ruleArray = self.parseRule(self.rule)
        
    # Change the rule
    def setRule(self,r):
        self.rule = r%self.max_rule
        self.ruleArray = self.parseRule(r)
    
    # Get the neighborhood of a cell as a list. Note that cell neighborhoods wrap (the first and last cells are neighbors).
    def Neighbors(self,m):
        return [(m-1)%self.size,m%self.size,(m+1)%self.size]
        
    # Given the state of a cell and it's neighbors, look up the updated state for the cell.
    def apply_rule(self,n):
        nbrs = self.Neighbors(n)
        state = 0
        for i in range(0,len(nbrs)):
            state += (self.cell_states**i)*self.present[nbrs[i]]
        return self.ruleArray[state]

    # Create a lookup table based on rule
    def parseRule(self, x):
        y = x % self.max_rule
        ret = [0 for i in range(0, self.num_states)]
        i = 0
        while(y>0):
            ret[i] = y%self.cell_states
            i = i + 1
            y = y - y%self.cell_states
            y = y/self.cell_states
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
