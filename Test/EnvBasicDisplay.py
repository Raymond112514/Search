import pygame
from environment import environment

"""
Environment Display Test:
    This files tests basic functionality of the graphics of the environment
"""

class environmentDisplay:

    GRID_SIZE = 25
    WALL_COLOR = (101, 163, 242)
    TARGET_COLOR = (242, 116, 101)
    BORDER_COLOR = (255, 255, 255)
    NODE_COLOR = (163, 197, 241)
    BACKGROUND_COLOR = (193, 193, 193)

    def __init__(self, width: int, height: int, target: tuple):
        self.screen = None
        self.env = environment(width, height, target)
        self.screenWidth = self.GRID_SIZE * width
        self.screenHeight = self.GRID_SIZE * height
        self.env.addWall((0, 0))
        self.env.addWall((0, 2))
        self.env.addWall((2, 2))
        self.env.addWall((3, 2))

    def initialize(self):
        for x in range(4):
            for y in range(4):
                print(f"The neighbor of {(x, y)} is {self.env.getNeighbors((x, y))}")

        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("Grid-Based Game")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.BACKGROUND_COLOR)
            for x in range(0, self.screenWidth, self.GRID_SIZE):
                pygame.draw.line(self.screen, self.BORDER_COLOR, (x, 0), (x, self.screenHeight))
            for y in range(0, self.screenHeight, self.GRID_SIZE):
                pygame.draw.line(self.screen, self.BORDER_COLOR, (0, y), (self.screenWidth, y))

            targetX, targetY = self.env.targetX, self.env.targetY
            self.drawRectangles(targetX, targetY, self.TARGET_COLOR)

            for wallX, wallY in self.env.getListOfWalls():
                self.drawRectangles(wallX, wallY, self.NODE_COLOR)

            pygame.display.flip()
            pygame.time.delay(150)

    def drawRectangles(self, posX: int, posY: int, color: tuple):
        rect = pygame.Rect(
                posX * self.GRID_SIZE, posY * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE
            )
        pygame.draw.rect(self.screen, color, rect)

display = environmentDisplay(20, 15, (4, 3))
display.initialize()