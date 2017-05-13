# Build the cellular automaton rule corresponding to Conway's game of life

# Convert rule from Golly/MCell notation to Wolfram code. 
def ConvertRule(birth, survival):
    ret = 0
    ruleArray = [0 for i in range(0,2**9)]
    stateArray = [0 for i in range(0,9)] 

    # For every possible state of a neighborhood, read off the successive state according to the rules of Conway's life and store the results in a lookup table
    for s in range(0,len(ruleArray)):
        r = int(s)
        for i in range(0,len(stateArray)):
            stateArray[i] = r%2
            r = r-stateArray[i]
            r = r/2
        # me is the cell who's state were updating. It corresponds to the fifth element of the list
        me = stateArray[4]
        num_nbrs = 0
        for i in range(0,len(stateArray)):
            num_nbrs = num_nbrs + stateArray[i]

        if me==0 and (num_nbrs in birth):
            ruleArray[s] = 1
        elif me==1 and ((num_nbrs - 1) in survival):
            ruleArray[s] = 1
        else:
            ruleArray[s] = 0

    #Convert the lookup table into a number
    for s in range(0,len(ruleArray)):
        ret += (ruleArray[s])*(2**s)
    return ret

# Find the game of life
def FindConwaysLife():
    birth = [3]
    survival = [2,3]
    return ConvertRule(birth, survival)

def Main():
    birth = [2,3]
    survival = [2,3]
    x = ConvertRule(birth, survival)
    print
    print x
    print
    return
    
if __name__ == "__main__":
    Main()
