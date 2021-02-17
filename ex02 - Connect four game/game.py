import copy
import alphaBetaPruning
import random

VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = -1  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board

rows = 6
columns = 7


class game:
    board = []
    size = rows * columns
    playTurn = HUMAN

    # Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''


def create(s):
    # Returns an empty board. The human plays first.
    # create the board
    s.board = []
    for i in range(rows):
        s.board = s.board + [columns * [0]]

    s.playTurn = HUMAN
    s.size = rows * columns
    s.val = 0.00001

    # return [board, 0.00001, playTurn, r*c]     # 0 is TIE


def cpy(s1):
    # construct a parent DataFrame instance
    s2 = game()
    s2.playTurn = s1.playTurn
    s2.size = s1.size
    s2.board = copy.deepcopy(s1.board)
    print("board ", s2.board)
    return s2


# *******************************
def value(s):
    # print("s.playTurn= " + str(s.playTurn))
    # Returns the heuristic value of s - if max wins returns 10**20,
    # if max looses returns -(10**20) and if it's tied returns -1

    z = 0

    # checks horizontal to the right
    for c in range(columns - 3):
        for r in range(rows):
            if r + 3 < columns:
                if s.board[r][c] == s.playTurn and s.board[r][c + 1] == s.playTurn and s.board[r][c + 2] == s.playTurn and s.board[r][c + 3] == s.playTurn:
                    if s.playTurn == 1:
                        z = LOSS
                    else:
                        z = VICTORY
    # print(z)

    # checks horizontal to the left
    for c in range(columns + 3, columns):
        for r in range(rows):
            # print("s.board[r][c]= " + str(s.board[r][c]))
            if s.board[r][c] == s.playTurn and s.board[r][c - 1] == s.playTurn and s.board[r][c - 2] == s.playTurn and s.board[r][c - 3] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY
    # print(z)

    # checks vertical up
    for c in range(columns):
        for r in range(rows + 3, rows):
            if s.board[r][c] == s.playTurn and s.board[r - 1][c] == s.playTurn and s.board[r - 2][c] == s.playTurn and s.board[r - 3][c] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY
    # print(z)

    # checks vertical down
    for c in range(columns):
        for r in range(rows - 3):
            if s.board[r][c] == s.playTurn and s.board[r + 1][c] == s.playTurn and s.board[r + 2][c] == s.playTurn and s.board[r + 3][c] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY
    # print(z)

    # checks diagonal left up
    for c in range(columns + 3, columns):
        for r in range(rows + 3, rows):
            if s.board[r][c] == s.playTurn and s.board[r - 1][c - 1] == s.playTurn and s.board[r - 2][c - 2] == s.playTurn and s.board[r - 3][c - 3] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY
    # print(z)

    # checks diagonal right up
    for c in range(columns - 3):
        for r in range(rows + 3, rows):
            if s.board[r][c] == s.playTurn and s.board[r - 1][c + 1] == s.playTurn and s.board[r - 2][c + 2] == s.playTurn and s.board[r - 3][c + 3] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY
    # print(z)

    # checks diagonal left down
    for c in range(columns + 3, columns):
        for r in range(rows - 3):
            if s.board[r][c] == s.playTurn and s.board[r + 1][c - 1] == s.playTurn and s.board[r + 2][c - 2] == s.playTurn and s.board[r + 3][c - 3] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY
    # print(z)

    # checks diagonal right down
    for c in range(columns - 3):
        for r in range(rows - 3):
            if s.board[r][c] == s.playTurn and s.board[r + 1][c + 1] == s.playTurn and s.board[r + 2][c + 2] == s.playTurn and s.board[r + 3][c + 3] == s.playTurn:
                if s.playTurn == 1:
                    z = LOSS
                else:
                    z = VICTORY

    if isfull(s):
        z = TIE  # if we got here it means no one has wan, it's a tie.
    # print(z)
    # *******************************
    # checks rows for two of the same kind, adds 3 for H subs 3 for C
    for x in range(rows):
        for y in range(columns):
            if y + 1 < columns:
                if s.board[x][y] == HUMAN and s.board[x][y + 1] == HUMAN:
                    z = z + 3
                if s.board[x][y] == COMPUTER and s.board[x][y + 1] == COMPUTER:
                    z = z - 3

    # checks columns for two of the same kind, adds 3 for H subs 3 for C
    for x in range(rows):
        for y in range(columns):
            if x + 1 < rows:
                if s.board[x][y] == HUMAN and s.board[x + 1][y] == HUMAN:
                    z = z + 3
                if s.board[x][y] == COMPUTER and s.board[x + 1][y] == COMPUTER:
                    z = z - 3

    # checks horizontal up left for two of the same kind, adds 3 for H subs 3 for C
    for x in range(rows):
        for y in range(columns):
            if x + 1 < rows and y - 1 >= 0:
                if s.board[x][y] == HUMAN and s.board[x + 1][y - 1] == HUMAN:
                    z = z + 3
                if s.board[x][y] == COMPUTER and s.board[x + 1][y - 1] == COMPUTER:
                    z = z - 3

    # checks horizontal up right for two of the same kind, adds 3 for H subs 3 for C
    for x in range(rows):
        for y in range(columns):
            if y + 1 < columns and x + 1 < rows:
                if s.board[x][y] == HUMAN and s.board[x + 1][y + 1] == HUMAN:
                    z = z + 3
                if s.board[x][y] == COMPUTER and s.board[x + 1][y + 1] == COMPUTER:
                    z = z - 3

    # checks rows for three of the same kind, adds 10 for H subs 10 for C
    for x in range(rows):
        for y in range(columns):
            if y + 2 < columns:
                if s.board[x][y] == HUMAN and s.board[x][y + 1] == HUMAN and s.board[x][y + 2] == HUMAN:
                    z = z + 10
                if s.board[x][y] == COMPUTER and s.board[x][y + 1] == COMPUTER and s.board[x][y + 2] == COMPUTER:
                    z = z - 10

    # checks columns for three of the same kind, adds 10 for H subs 10 for C
    for x in range(rows):
        for y in range(columns):
            if x + 2 < rows:
                if s.board[x][y] == HUMAN and s.board[x + 1][y] == HUMAN and s.board[x + 2][y] == HUMAN:
                    z = z + 10
                if s.board[x][y] == COMPUTER and s.board[x + 1][y] == COMPUTER and s.board[x + 2][y] == COMPUTER:
                    z = z - 10

    # checks horizontal up left for three of the same kind, adds 10 for H subs 10 for C
    for x in range(rows):
        for y in range(columns):
            if x + 2 < rows and y - 2 >= 0:
                if s.board[x][y] == HUMAN and s.board[x + 1][y - 1] == HUMAN and s.board[x + 2][y - 2] == HUMAN:
                    z = z + 10
                if s.board[x][y] == COMPUTER and s.board[x + 1][y - 1] == COMPUTER and s.board[x + 2][y - 2] == COMPUTER:
                    z = z - 10

    # checks horizontal up right for two of the same kind, adds 10 for H subs 10 for C
    for x in range(rows):
        for y in range(columns):
            if y + 2 < columns and x + 2 < rows:
                if s.board[x][y] == HUMAN and s.board[x + 1][y + 1] == HUMAN and s.board[x + 2][y + 2] == HUMAN:
                    z = z + 10
                    print(z)
                if s.board[x][y] == COMPUTER and s.board[x + 1][y + 1] == COMPUTER and s.board[x + 2][y + 2] == COMPUTER:
                    z = z - 10
                    print(z)

    return z


def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.

    for x in range(rows):
        for y in range(columns):
            if s.board[x][y] == 0:
                act = 0
            elif s.board[x][y] == HUMAN:
                act = "O"
            elif s.board[x][y] == COMPUTER:
                act = "X"
            print(' %s |' % act, end='')
        print("\n")
    """for r in range(rows):
            print("\n|", end = "")
            # print("\n", len(s[0][0])*" --", "\n|", sep="", end="")
            for c in range(columns):
                if s.board[r][c] == COMPUTER:
                    print("X|", end = "")
                elif s.board[r][c] == HUMAN:
                    print("O|", end = "")
                else:
                    print(" |", end = "")
        print()

        for i in range(columns):
            print(" ", i, sep = "", end = "")
        print()"""

    val = value(s)
    if val == VICTORY:
        print("I won!")
    elif val == LOSS:
        print("You beat me!")
    elif val == TIE:
        print("It's a TIE")


def isfull(s):
    # Returns True if the board is full
    for x in range(rows):
        for y in range(columns):
            if s.board[x][y] == 0:
                return 0
    return 1


def isFinished(s):
    # Returns True if the game ended
    return value(s) in [LOSS, VICTORY, TIE] or isfull(s) == 1  # f,0

def isHumTurn(s):
    # Returns True if it is the human's turn to play
    return s.playTurn == HUMAN


def decideWhoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me (computer) / anything else-you (human) : ")) == 1:
        s.playTurn = COMPUTER
    else:
        s.playTurn = HUMAN

    print(s.playTurn)
    return s.playTurn


def makeMove(s, c):
    # Puts mark (for huma. or comp.) in col. c
    # and switches turns.
    # Assumes the move is legal.

    r = 0
    while r < rows and s.board[r][c] == 0:
        r += 1

    s.board[r - 1][c] = s.playTurn  # marks the board
    s.size -= 1  # one less empty cell
    if s.playTurn == COMPUTER:
        s.playTurn = HUMAN
    else:
        s.playTurn = COMPUTER


def inputMove(s):
    # Reads, enforces legality and executes the user's move.

    # self.printState()
    flag = True
    while flag:
        c = int(input("Enter your next move: (insert the number of column you choose (0-6)) "))
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")
        else:
            flag = False
            makeMove(s, c)


def getNext(s):
    # returns a list of the next states of s
    ns = []
    for c in list(range(columns)):
        print("c=", c)
        if s.board[0][c] == 0:
            print("possible move ", c)
            tmp = cpy(s)
            makeMove(tmp, c)
            print("tmp board=", tmp.board)
            ns += [tmp]
            print("ns=", ns)
    print("returns ns ", ns)
    return ns


def inputComputer(s):
    return alphaBetaPruning.go(s)
