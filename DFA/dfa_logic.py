class State:
    def __init__(self, name, isFinal=False):
        self.name = name    #Name of state
        self.transitions = {}   # Dictionary to store transitions
        self.isFinal = isFinal  # Final state
        self.accepted_counts = {}  # Counter - Dictionary to store occurance counts of accepted strings
        
    # Adds transition from the current state to the next state (based on the input character)
    def addTransition(self, input, nextState):
        self.transitions[input] = nextState

    # Retrieve next state based on input character
    def getNextState(self, char):
        return self.transitions.get(char)
    
    # Take an input string, enter the DFA, then returns accepted or rejected along with transition path 
    def testInput(self, input):
        currentState = self
        path = ""
        for char in input:
            nextState = currentState.getNextState(char)
            if nextState:
                currentState = nextState
                path += f"{char} -> "
            else:
                path += f"{char} -> Rejected"
                return (False, path)
        if currentState.isFinal:
            path = path[:-3] + " -> Accepted" #[:-3] for removing "-> "
            # Increment count for the accepted string
            accepted_str = currentState.name
            self.accepted_counts[accepted_str] = self.accepted_counts.get(accepted_str, 0) + 1
        else:
            path += "Rejected"
        return (currentState.isFinal, path)

# Build dfa for recognize specific words (accepted words)
def build_dfa():
    start = State("start") # Define start state
    # Define accepted words
    words = ["bread", 
             "curry",
             "hokkien_mee",
             "mee_goreng",
             "meat",
             "murtabak", 
             "nasi_kandar", 
             "noodle", 
             "rice", 
             "roti_canai", 
             "roti_jala", 
             "roti_tisu", 
             "snack", 
             "spices",
             "tea",
             "teh_tarik",
             "vegetables"]
    # Iterate over each word in accepted word list
    for word in words:
        # Define start state for each word
        currentState = start
        # Iterate over each character in the word, with its index
        for i, char in enumerate(word):
            if char not in currentState.transitions:
                newState = State(word[:i+1], i == len(word) - 1) # State(name, is final)
                currentState.addTransition(char, newState)
            currentState = currentState.transitions[char]

    return start, words

# For line 64
#name, (i== len(word) - 1) detect is final state or not
#bread[:0+1] = b
#bread[:0+2] = br ......, it will produce b -> br -> bre -> brea -> bread  