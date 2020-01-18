import sys
from os import path
from random import randint
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.markov import World

class MarkovTest():
    def __init__(self, gamma = None, eps = None, L = None, H = None):

        if eps == None:
            self.eps = 0.01
        else:
            self.eps = eps
        
        if gamma == None:
            self.gamma = 0.99
        else:
            self.gamma = gamma

        if L == None:
            self.L = 6
        else:
            self.L = L
        
        if H == None:
            self.H = 5
        else:
            self.L = L

        self.mark = World(self.L, self.H, 0)
        self.utilities, self.iterations = self.mark.computeUtility(self.gamma, self.eps)

def test_utilities():
    mark_test = MarkovTest()
    for elem in mark_test.utilities:
        assert elem >= 0 or elem == -1

def test_iterations():
    mark_test = MarkovTest()
    assert mark_test.iterations > 0 and mark_test.iterations >= (mark_test.H * mark_test.L / 2 - 1)

def test_attributes():
    mark_test = MarkovTest()
    assert (mark_test.gamma + mark_test.eps) == 1