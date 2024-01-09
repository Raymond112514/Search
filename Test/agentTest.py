from unittest import TestCase
from environment import environment
from agent import agent

class testBasicAgent(TestCase):

    def setUp(self) -> None:
        self.env = environment(100, 75, (1, 1))
        self.agent = agent(self.env, (0, 0))
        self.env.addWall((0, 2))
        self.env.addWall((2, 2))
        self.env.addWall((3, 2))

    def testValidate(self):
        assert self.agent.validate((-1, 0)) is False
        assert self.agent.validate((0, 67)) is True
        assert self.agent.validate((101, 32)) is False
        assert self.agent.validate((25, 75)) is False

    def testGetSuccessors(self):
        assert self.agent.getSuccessors((0, 0)) == [(1, 0), (0, 1)]
        assert self.agent.getSuccessors((1, 0)) == [(2, 0), (1, 1), (0, 0)]
        assert self.agent.getSuccessors((1, 1)) == [(1, 0), (2, 1), (1, 2), (0, 1)]
        assert self.agent.getSuccessors((2, 1)) == [(2, 0), (3, 1), (1, 1)]
