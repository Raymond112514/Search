from agent import agent

class dfsAgent(agent):

    def search(self):
        self.depthFirstSearch()
        self.getPath()
        print(f"Nodes explored: {len(self.visited)}")

    """
    depthFirstSearch
        Implements the depth first search algorithm
    """
    def depthFirstSearch(self):
        fringe = [self.position]
        while len(fringe) != 0:
            position = fringe.pop()
            self.visited.append(position)
            if self.isTerminal(position):
                self.solutionExists = True
                break
            for successor in self.getSuccessors(position):
                if successor not in self.visited:
                    self.prev[successor] = position
                    fringe.append(successor)
