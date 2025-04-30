import random # randomly generate 2 or 4 tiles
import copy # deepcopying board

"""
copy module creates either shallow or deep copies

shallow: copy of the original, but nested objects references original;
modifying the nested objects in the shallow copy will also affect the original object
(conceptually similar to using pointers in C)

deep: duplicates the entire object hierarchy, creating independent copies of all nested objects;
modifying the nested objects in the deep copy will not affect the original object

we use deepcopy to avoid shared references, allowing us to effectively create an undo function
"""


class BoardState:
    def __init__(self):
        self.board = None # placeholder value
        self.previousStates = [] # stack to store previous board states

    def saveState(self): # saves the current board state to the stack
        self.previousStates.append(copy.deepcopy(self.board))

    def undo(self): # restores the last saved board state
        if self.previousStates:
            self.board = self.previousStates.pop()
            return True # undo successful
        return False # no states to undo
    
"""
utilizes a stack data structure (LIFO behavior)
: most recent board state is the first one to be restored;
stack ensures the last saved state is always to first one to be retrieved

push: adds an element to the top of the stack
pop: remove the element from the top of the stack
both operations are of time complexity O(1) (constant time), making this time efficient vs.
a data structure like a queue (FIFO beahvior) which is of time complexity O(n)
"""


def reset(boardState):
    boardState.board = initBoard() # resets the board to its initial state
    boardState.previousStates = [] # clears undo history
    print("Game has been reset!")

"""
utiizes BoardState class to implement reset feature
"""


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

"""formatting the board in the terminal"""
