def initBoard():

    emptyRow = [0, 0, 0, 0] # create a list of empty row values
    board = [] # create an empty list to hold the rows

    # initialize empty board
    for i in range(4):
        board.append(emptyRow[:])  # slicing the list to create copies

    return board

"""
modifying emptyRow would modify every row in the board so,
[:] ensures each row in the board becomes an independent copy of emptyRow;
"""


def printBoard(board): # board is passed in as an argument

    print("\n") # spacing between each board

    for row in board:
        printedRow = [] # holder variable to be printed

        for cell in row:

            if cell == 0:
                printedRow.append(" -".rjust(5)) # 0 or empty is represented as - for readability

            else:
                printedRow.append(str(cell).rjust(5)) # .rjust(n) adds n spaces to the left of the str

        print(" ".join(printedRow)) # concatentates the elements of the each row
        print("\n") # spacing between each row