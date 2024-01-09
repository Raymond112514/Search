from environment import environment

class agent:

    ACTIONS = ["N", "E", "S", "W"]

    def __init__(self, env: environment, spawnpoint: tuple):
        self.env = env
        self.position = spawnpoint
        self.spawnpoint = spawnpoint
        self.visited = []
        self.prev = {spawnpoint: None}
        self.solutionExists = False
        self.path = None
        self.distTo = self.distTo = {self.spawnpoint: 0}

    """
    getSuccessors:
        Returns a list of successors given current position
    """
    def getSuccessors(self, position: tuple):
        successors = []
        for action in self.ACTIONS:
            successor = self.getSuccessorState(position, action)
            if self.env.validate(successor) and not self.env.isWall(successor):
                successors.append(successor)
        return successors

    """
    getSuccessorState:
        Given current position and action taken, returns the new successor state 
        If the action is not feasible, return None
    """
    def getSuccessorState(self, position, action):
        if action == "N":
            return position[0], position[1] - 1
        elif action == "S":
            return position[0], position[1] + 1
        elif action == "W":
            return position[0] - 1, position[1]
        elif action == "E":
            return position[0] + 1, position[1]
        else:
            return None

    """
    isTerminal:
        Returns true is the current position is the terminal state
    """
    def isTerminal(self, position: tuple):
        return self.env.isTerminal(position)

    """
    search:
        Search method, implementation depends on types of agent.
        After the search is complete, getPath should be called to update the path to target
        Provided that the solution exists
    """
    def search(self):
        pass

    """
    getPath:
        Updates the path to solution provided that a solution exists
    """
    def getPath(self):
        if self.solutionExists:
            path = []
            state = self.env.target
            while state is not None:
                path.append(state)
                state = self.prev[state]
            path.reverse()
            self.path = path

    """
    getCost:
        Returns the cost of current position
    """
    def getCost(self, position):
        pass

    """
    heuristic:
        Heuristic function for informed search
    """
    def heuristic(self, position):
        pass





