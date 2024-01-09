import random

class environment:

    ACTIONS = ["N", "E", "S", "W"]

    def __init__(self, width, height, target: tuple):
        self.width = width
        self.height = height
        self.target = target
        self.walls = set()
        self.numWalls = 0

    """
    addWall:
        Takes in a location tuple and adds a wall at the location
        Returns the total number of walls
    """
    def addWall(self, location: tuple) -> int:
        if location not in self.walls:
            self.walls.add(location)
            self.numWalls += 1
        return self.numWalls

    """
    getNeighbors:
        Takes in a location and returns a list of neighbors that are in the grid and is not a wall
        The neighbors are tuples (not vectors)
    """
    def getNeighbors(self, location: tuple) -> list:
        neighbors = []
        for x in [location[0] - 1, location[0] + 1]:
            if self.validate((x, location[1])) and (x, location[1]) not in self.walls:
                neighbors.append((x, location[1]))
        for y in [location[1] - 1, location[1] + 1]:
            if self.validate((location[0], y)) and (location[0], y) not in self.walls:
                neighbors.append((location[0], y))
        return neighbors

    """
    validate:
        Takes in a location and returns whether the proposed location is valid
    """
    def validate(self, location: tuple) -> bool:
        return 0 <= location[0] < self.width and 0 <= location[1] < self.height

    """
    isWall:
        Returns true if the current location is a wall
    """
    def isWall(self, location: tuple) -> bool:
        return location in self.walls

    """
    getListOfWalls
        Returns the list of walls in tuple
    """
    def getListOfWalls(self) -> list:
        return list(self.walls)

    """
    isTerminal:
        Retunrs true if the current location is the target state
    """
    def isTerminal(self, location) -> bool:
        return location == self.target

    """
    setRandomSeed
        Generates a random set of walls based on the coverage ratio
    """
    def setRandomSeed(self, coverageRatio):
        numGrids = self.width * self.height
        numWalls = round(numGrids * coverageRatio)
        walls = set()
        while len(walls) != numWalls:
            randX = random.randint(0, self.width - 1)
            randY = random.randint(0, self.height - 1)
            if (randX, randY) not in walls and (randX, randY) != self.target:
                walls.add((randX, randY))
        self.walls = list(walls)

