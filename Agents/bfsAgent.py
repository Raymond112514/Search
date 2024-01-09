from agent import agent
from collections import deque

class bfsAgent(agent):

    def search(self):
        self.breadthFirstSearch()
        self.getPath()
        print(f"Nodes explored: {len(self.visited)}")

    """
    breadthFirstSearch
        Implements the breadth first search algorithm
    """
    def breadthFirstSearch(self):
        fringe = deque([self.position])
        while len(fringe) != 0:
            node = fringe.popleft()
            if node not in self.visited:
                self.visited.append(node)
            if self.isTerminal(node):
                self.solutionExists = True
                break
            for successor in self.getSuccessors(node):
                if successor not in self.visited:
                    self.prev[successor] = node
                    fringe.append(successor)