# Example of World building, display, and successor computation for the artificial 
# intelligence path-finding lab
#
# Author: Didier Lime
# Date: 2018-10-03

from random import random
from sys import stdout

class World:
    # initialise the world

    # L is the number of columns
    # H is the number of lines
    # P is the probability of having a wall in a given tile
    def __init__(self, L, H, P):
        self.L = L 
        self.H = H
        self.value = [0 for i in range(L*H)] # initialise every tile to empty (0)

        # the World is represented by an array with one dimension
        self.w = [0 for i in range(L*H)] # initialise every tile to empty (0)

        # add walls in the first and last columns
        for i in range(H):
            self.w[i*L] = 1
            self.w[i*L+L-1] = 1
        
        # add walls in the first and last lines
        for j in range(L):
            self.w[j] = 1
            self.w[(H-1)*L + j] = 1

        # generate the write markov matrix
        self.w[14] = 1

        # insert values for tiles
        for i in range (H*L) :
            if self.w[i] == 0 :
                self.value[i] = -0.04
            self.value[10] = 1
            self.value[16] = -1
       


    # display the World
    def display(self):
        for i in range(self.H):
            for j in range(self.L):
                if self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')

            print('')

    def display_path(self, path):
        for i in range(self.H):
            for j in range(self.L):
                if (self.w[i * self.L + j] == 0) and (i * self.L + j) not in path :
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')
                elif (self.w[i * self.L + j] == 0) and (i * self.L + j) in path :
                    stdout.write('*')

            print('')

    # compute the successors of tile number i in World w
    def successors(self, i):
        if i < 0 or i >= self.L * self.H or self.w[i] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return [] 
        else:
            # look in the four adjacent tiles and keep only those with no wall
            return list(filter(lambda x: self.w[x] != 1, [i - 1, i + 1, i - self.L, i + self.L]))

    def computeUtility(self, gamma, epsilon):
        utility = [0 for i in range (self.H*self.L)]
        current_utility = [0 for i in range (self.H*self.L)]
        condition = epsilon*(1-gamma)/gamma
        iteration = 0
        test = [False for i in range (self.H*self.L)]
        for i in range (self.H*self.L) :
            current_utility[i] = self.value[i]
        
        while not all(elem == True for elem in test) :
            i = 0
            test = [False for i in range (self.H*self.L)]
            while i < (self.H*self.L) :
                utility = current_utility[:]
                if self.w[i] == 1:
                    test[i] = True
                
                else:
                    if ( i == 7 or i == 19 or i == 22 ):
                        children = self.successors(i)
                        current_utility[i]=self.value[i]+gamma*max(0.8*utility[children[0]]+0.1*utility[children[1]]+0.1*utility[i],
                                                        0.8*utility[children[1]]+0.1*utility[children[0]]+0.1*utility[i],
                                                        0.8*utility[i]+0.1*utility[children[1]]+0.1*utility[i],
                                                        0.8*utility[i]+0.1*utility[children[0]]+0.1*utility[i])
                    elif ( i == 8 or i == 13 or i == 20) :
                        children = self.successors(i)
                        current_utility[i]=self.value[i]+gamma*max(0.8*utility[children[0]]+0.1*utility[i]+0.1*utility[i],
                                                        0.8*utility[children[1]]+0.1*utility[i]+0.1*utility[i],
                                                        0.8*utility[i]+0.1*utility[children[1]]+0.1*utility[children[0]],
                                                        0.8*utility[i]+0.1*utility[children[0]]+0.1*utility[children[1]])
                    elif ( i == 9 or i == 21):
                        children = self.successors(i)
                        current_utility[i]=self.value[i]+gamma*max(0.8*utility[children[0]]+0.1*utility[i]+0.1*utility[children[2]],
                                                        0.8*utility[children[1]]+0.1*utility[i]+0.1*utility[children[2]],
                                                        0.8*utility[children[2]]+0.1*utility[children[1]]+0.1*utility[children[0]],
                                                        0.8*utility[i]+0.1*utility[children[0]]+0.1*utility[children[1]])
                    elif ( i == 15):
                        children = self.successors(i)
                        current_utility[i]=self.value[i]+gamma*max(0.8*utility[children[0]]+0.1*utility[children[1]]+0.1*utility[children[2]],
                                                        0.8*utility[children[1]]+0.1*utility[i]+0.1*utility[children[0]],
                                                        0.8*utility[children[2]]+0.1*utility[children[0]]+0.1*utility[i],
                                                        0.8*utility[i]+0.1*utility[children[2]]+0.1*utility[children[1]])
                    elif ( i == 10 or i == 16) :
                        test[i] = True
                    if abs(current_utility[i]-utility[i]) <= condition :
                        test[i] = True
                # print(test)
                i = i +1
            iteration = iteration + 1
        return current_utility, iteration

if __name__ == "__main__":
    # create a World
    w = World(6, 5, 0)
    U, k = w.computeUtility(0.99,0.01)


    # display it 
    w.display()

    print(U)
    print(k)
