from dfsAgent import dfsAgent
from environment import environment

env = environment(5, 5, (3, 3))
env.addWall((0, 1))
env.addWall((1, 1))
env.addWall((2, 1))
agent = dfsAgent(env, (0, 0))
agent.search()