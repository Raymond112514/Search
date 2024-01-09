import pygame
from agent import agent
from environment import environment

class graphics:

    GRID_SIZE = 25
    WALL_COLOR = (96, 96, 96)
    START_COLOR = (101, 163, 242)
    TARGET_COLOR = (242, 116, 101)
    BORDER_COLOR = (255, 255, 255)
    PATH_COLOR = (131, 184, 252)
    NODE_COLOR = (163, 197, 241)
    COLOR = (172, 162, 150)
    BACKGROUND_COLOR = (193, 193, 193)
    DELAY = 150

    def __init__(self, env: environment, ag: agent):
        self.screen = None
        self.env = env
        self.agent = ag
        self.WIDTH = self.GRID_SIZE * self.env.width
        self.HEIGHT = self.GRID_SIZE * self.env.height
        self.target = self.env.target
        self.explored, self.path = [], []

    """
    run:
        Main loop
    """
    def run(self):
        self.agent.search()
        exploredIter, n_explored = self.makeIterable(self.agent.visited)
        pathIter, n_path = self.makeIterable(self.agent.path)
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
            self.screen.fill(self.BACKGROUND_COLOR)
            self.grid()
            self.fillWall()
            self.fillExplored()
            if n_explored != 1:
                self.explored.append(next(exploredIter))
                n_explored -= 1
            else:
                if n_path != 1:
                    self.path.append(next(pathIter))
                    n_path -= 1
                self.fillPath()
            self.fill(self.agent.spawnpoint, self.START_COLOR)
            self.fill(self.target, self.TARGET_COLOR)
            pygame.display.flip()
            pygame.time.delay(self.DELAY)

    """
    makeIterable:
        Given a path, returns an iterator of the path and the length of the path
    """
    def makeIterable(self, path: list):
        return iter(path), len(path)

    """
    fill:
        On the screen, fill a grid block at the specified position with the specified color 
    """
    def fill(self, pos: tuple, color: tuple):
        posX = pos[0] * self.GRID_SIZE
        posY = pos[1] * self.GRID_SIZE
        rect = pygame.Rect(
                posX, posY, self.GRID_SIZE, self.GRID_SIZE
            )
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.line(self.screen, self.BORDER_COLOR, (posX, posY), (posX, posY + self.GRID_SIZE), 1)
        pygame.draw.line(self.screen, self.BORDER_COLOR, (posX, posY), (posX + self.GRID_SIZE, posY), 1)

    """
    grid:
        On the screen outlines the gird
    """
    def grid(self):
        for x in range(0, self.WIDTH, self.GRID_SIZE):
            pygame.draw.line(self.screen, self.BORDER_COLOR, (x, 0), (x, self.HEIGHT), 1)
        for y in range(0, self.HEIGHT, self.GRID_SIZE):
            pygame.draw.line(self.screen, self.BORDER_COLOR, (0, y), (self.WIDTH, y), 1)

    """
    grid:
        On the screen fill the walls
    """
    def fillWall(self):
        for node in self.env.getListOfWalls():
            self.fill(node, self.WALL_COLOR)

    """
    fillExplored:
        On the screen fill the explored nodes
    """
    def fillExplored(self):
        for node in self.explored:
            self.fill(node, self.NODE_COLOR)

    """
    fillPath:
        On the screen fill the path nodes
    """
    def fillPath(self):
        for node in self.path:
            self.fill(node, self.PATH_COLOR)

