import game

# creates a new board for the game
board = game.game()
game.create(board)
print("Initial Game")

# prints the current board
game.printState(board)

# decides who is playing first - human or computer
game.decideWhoIsFirst(board)

# runs the game until it's finished with a winner or a tie
while not game.isFinished(board):
    print("continue game")
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        board = game.inputComputer(board)
    game.printState(board)

print("Game Over:")

