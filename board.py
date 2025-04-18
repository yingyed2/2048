import random # randomly generate 2 or 4 tiles


def placeRandomTile(board):

    emptyPositions = [] # list to store the positions of empty tiles
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0: # checking if position is empty
                emptyPositions.append((row, col)) # adding empty positions to list

    if len(emptyPositions) == 0:
        return # exits the function if there are no empty tiles

    randomPosition = random.choice(emptyPositions) # function from random module to select from empty list
    row, col = randomPosition # defines the selected position as row and column indices

    randomValue = random.random() # generate a random float between 0 and 1
    if randomValue < 0.9:
        tileValue = 2 # 90% to place 2
    else:
        tileValue = 4 # 10% to place 4

    board[row][col] = tileValue # places the tileValue into the randomPosition

"""
utilizes the random module, using the random.choice and random.random functions
to generate a random value tile onto a random position of the board
"""


def initBoard():

    emptyRow = [0, 0, 0, 0] # create a list of empty row values
    board = [] # create an empty list to hold the rows

    # initialize empty board
    for i in range(4):
        board.append(emptyRow[:]) # slicing the list to create copies

    placeRandomTile(board)
    placeRandomTile(board)

    return board

"""
modifying emptyRow would modify every row in the board so,
[:] ensures each row in the board becomes an independent copy of emptyRow;
"""


def printBoard(board): # board is passed in as an argument

    print("\n") # spacing between each board

    for row in board:
        printedRow = [] # holder variable to be printed

        for tile in row:

            if tile == 0:
                printedRow.append(" -".rjust(5)) # 0 or empty is represented as - for readability

            else:
                printedRow.append(str(tile).rjust(5)) # .rjust(n) adds n spaces to the left of the str

        print(" ".join(printedRow)) # concatentates the elements of the each row
        print("\n") # spacing between each row