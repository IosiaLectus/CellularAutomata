# Build the cellular automaton rule corresponding to Conway's game of life

# Convert rule from Golly/MCell notation to Wolfram code.
def ConvertRule(birth, survival):
    ret = 0
    ruleArray = [0 for i in range(0,2**9)]
    stateArray = [0 for i in range(0,9)]

    # For every possible state of a neighborhood, read off the successive state according to the MCell and store the results in a lookup table
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

# Find rules where the updated state of a cell is an affine function of the states of the cell's neighbors (and the cell's own state). This seems to take a very long time to run.
def AffineRule(n_states, n_nbrs, m, b):
    # Number of possible states of a neighborhood:
    n_nbhd_states = n_states**n_nbrs

    # m is interpreted as a base n_states integer, which in turn is interpreted as a vector base n_states digits which will be used as the multiplicative parameters in the affine function
    mm = int(m)
    m_list = [0 for i in range(0, n_nbrs)]
    for i in range(0, n_nbrs):
        x = mm % n_states
        m_list[i] = x
        mm = (mm - x)/n_states

    # Now we will write out the rule array
    rule_array = [0 for i in range(0, n_nbhd_states)]
    state_array = [0 for i in range(0,n_nbrs)]

    # For every possible state of a neighborhood, read off the successive state according to the affine rule and store the results in a lookup table
    for s in range(0,len(rule_array)):
        r = int(s)
        for i in range(0,len(state_array)):
            state_array[i] = r%n_states
            r = r-state_array[i]
            r = r/n_states
        # Compute the affine function
        rule_array[s] = b % n_states
        for i in range(0, n_nbrs):
            rule_array[s] = (rule_array[s] + m_list[i]*state_array[i]) % n_states

    ret = 0
    #Convert the lookup table into a number
    for s in range(0,len(rule_array)):
        ret += (rule_array[s])*(n_states**s)
    return ret

def Main():
    print(FindConwaysLife())

if __name__ == "__main__":
    Main()
