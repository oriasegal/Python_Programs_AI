"""
Oria Segal
209338193
"""

'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''

import random
import math

# returns a random board nXn


def create(n):
    s = list(range(n*n))  # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m = "<>v^"  # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n*n*n):  # makes n^3 random moves
        if_legal(s, m[random.randrange(4)])  # checks if its a legal move to do
    return [s, ""]


def get_next(x):  # returns a list of the children states of x
    ns = []  # the next state list
    for i in "<>v^":
        s = x[0][:]  # [:] - copies the board in x[0]
        if_legal(s, i)  # try to move in direction i
        # checks if the move was legal and...
        if s.index(0) != x[0].index(0) and \
           (x[1] == "" or x[1][-1] != "><^v"["<>v^".index(i)]):  # check if it's the first move or it's a reverse move
            ns.append([s, x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):  # returns the length of the paths we've done
    return len(x[1])


def is_target(x):  # did we get to the last move - did we finish the game
    n = len(x[0])  # the size of the board
    return x[0] == list(range(n))  # list(range(n)) is the target state


#############################
def if_legal(x, m):  # gets a board and a move and makes the move if it's legal
    n = int(math.sqrt(len(x)))  # the size of the board is nXn
    z = x.index(0)  # z is the place of the empty tile (0)
    if z % n > 0 and m == "<":  # checks if the empty tile is not in the first col and the move is to the left
        x[z] = x[z-1]  # swap x[z] and x[z-1]...
        x[z-1] = 0     # ...and move the empty tile to the left
    elif z % n < n-1 and m == ">":  # check if the empty tile is not in the n's col and the move is to the right
        x[z] = x[z+1]
        x[z+1] = 0
    elif z >= n and m == "^":  # check if the empty tile is not in the first row and the move is up
        x[z] = x[z-n]
        x[z-n] = 0
    elif z < n*n-n and m == "v":  # check if the empty tile is not in the n's row and the move is down
        x[z] = x[z+n]
        x[z+n] = 0


def hdistance(s):  # the heuristic value of s
    return 0  # at first, when we aren't using any heuristic functions on the algorithm

"""
def hdistance(s):  # the heuristic value of s
    # question 3 - the function is returning the number of blocks that aren't in their place
    blocks = 0
    k = 0
    for i in range(len(s) - 1):
        for j in range(len(s) - 1):
            if s[i][j] != k:
                blocks += 1
            k += 1
    return blocks
"""

"""
def hdistance(s):  # the heuristic value of s
    # question 5 - the function is returning the manhattan distance of the blocks
    distance = 0
    for i in range(len(s) - 1):
        for j in range(len(s) - 1):
            if s[i][j] != 0:
                # while s[i][j] == int:
                x = divmod(s[i][j], 3)
                distance += (x[0] - i) + (x[1] - j)
    return distance
"""

