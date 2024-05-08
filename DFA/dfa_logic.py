
class State:
    def __init__(self, name, isFinal=False):
        self.name = name
        self.transitions = {}
        self.isFinal = isFinal

    def addTransition(self, input, nextState):
        self.transitions[input] = nextState

    def getNextState(self, char):
        return self.transitions.get(char)

    def testInput(self, input):
        currentState = self
        path = ""
        for char in input:
            nextState = currentState.getNextState(char)
            if nextState:
                currentState = nextState
                path += f"{char} > "
            else:
                path += f"{char} > Rejected"
                return (False, path)
        if currentState.isFinal:
            path = path[:-3] + " > Accepted"
        else:
            path += "Rejected"
        return (currentState.isFinal, path)

def build_dfa():
    start = State("start")
    words = ["bread", 
             "curry", 
             "mee_goreng", 
             "murtabak", 
             "nasi_kandar", 
             "noodle", 
             "rice", 
             "roti_canai", 
             "roti_jala", 
             "roti_tisu", 
             "snack", 
             "spices", 
             "teh_tarik",
             "vegetables",
             "meat"]
    
    for word in words:
        currentState = start
        for i, char in enumerate(word):
            if char not in currentState.transitions:
                newState = State(word[:i+1], i == len(word) - 1)
                currentState.addTransition(char, newState)
            currentState = currentState.transitions[char]

    return start
