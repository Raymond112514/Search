from GreedyAgent import GreedyAgent
from environment import environment
from graphics import graphics

env = environment(15, 15, (12, 5))
env.setRandomSeed(0.2)
agent = GreedyAgent(env, (1, 10))
graphics = graphics(env, agent)
graphics.run()
