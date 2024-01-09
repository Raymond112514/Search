from bfsAgent import bfsAgent
from environment import environment
from graphics import graphics

env = environment(15, 15, (12, 5))
env.setRandomSeed(0.2)
agent = bfsAgent(env, (10, 10))
graphics = graphics(env, agent)
graphics.run()
