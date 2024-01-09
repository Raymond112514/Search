from agent import agent
from PriorityQueue import PriorityQueue

class GreedyAgent(agent):

    def search(self):
        self.GreedySearch()
        self.getPath()
        print(f"Nodes explored: {len(self.visited)}")

    def GreedySearch(self):
        fringe = PriorityQueue({self.spawnpoint: self.getCost(self.position)})
        while fringe.size() != 0:
            position = fringe.pop()
            self.visited.append(position)
            if self.isTerminal(position):
                self.solutionExists = True
                break
            for successor in self.getSuccessors(position):
                if successor not in self.visited:
                    self.prev[successor] = position
                    fringe.push(successor, self.getCost(successor))

    def getCost(self, position):
        return self.heuristic(position)

    def heuristic(self, position):
        return abs(self.env.target[0] - position[0]) + abs(self.env.target[1] - position[1])

