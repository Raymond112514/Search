from bfsAgent import bfsAgent
from environment import environment

env = environment(5, 5, (3, 3))
env.addWall((0, 1))
env.addWall((1, 1))
env.addWall((2, 1))
agent = bfsAgent(env, (1, 1))
agent.search()