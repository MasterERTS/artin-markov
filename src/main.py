import sys
from os import path
from random import randint
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.markov import World

# create a world
w = World(6, 5, 0)
U, k = w.computeUtility(0.99,0.01)
# display it 
w.display()
print(U)
print(k)