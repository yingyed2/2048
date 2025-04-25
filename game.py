def shiftingMerging(row):

    """removing zeroes from rows"""
    nonZeroTiles = [] # list to store all non-zero tiles
    for tile in row:
        if tile != 0:
            nonZeroTiles.append(tile)

    mergedTiles = []  # list to store the merged row
    skip = False  # flag to skip the next tile after a merge

    for i in range(len(nonZeroTiles)):
        if skip:  # if the previous tile is merged, skip to next index
            skip = False
            continue # this if block is skipped if true

        """if the current tile is not the last tile, and the current tile is equal to the next tile"""
        if i < len(nonZeroTiles) - 1 and nonZeroTiles[i] == nonZeroTiles[i + 1]:
            mergedTiles.append(nonZeroTiles[i] * 2)  # merge the tiles
            skip = True  # skips the next tile since it was merged
        else:
            mergedTiles.append(nonZeroTiles[i]) # as-is if unmergeable

    while len(mergedTiles) < len(row): # ensures correct row length
        mergedTiles.append(0) # append zeros to the end of the merged row

    # return the final merged row
    return mergedTiles

"""
* logic is based on left movement
only non-zero tiles are considered when shifting or merging, appended to a list nonZeroTiles[]
nonZeroTiles[] used to merge similar adjacent indices, utilizing a flag variable skip to prevent reptition
0s are added to the remaining indices to fulfill the correct row length

e.g.
original: [2,0,2,4]
nonZeroTiles: [2,2,4] (skips second index since first was already merged)
mergedTiles: [4,4,0,0]
"""


def moveTiles(board, direction):

    """helper function to transpose the board (swap rows and columns)"""
    def transpose(matrix):
        transposed = []

        for col in range(len(matrix[0])): # iterates length times of the first row of the matrix
            newRow = []

            for row in range(len(matrix)): # iterate over # of rows in the matrix
                newRow.append(matrix[row][col]) # collect elements from each row at the current column

            transposed.append(newRow)

        return transposed

    """helper function to reverse each row in the board"""
    def reverse(matrix):
        reversed = []

        for row in matrix: # iterate over each row in the matrix
            reversedRow = [] # create a new list for the reversed row

            for i in range(len(row) - 1, -1, -1): # iterate over the row in reverse order
                reversedRow.append(row[i])

            reversed.append(reversedRow)

        return reversed


    newBoard = []

    if direction == 'left': # default
        newBoard = [] 

        for row in board:
            mergedRow = shiftingMerging(row)
            newBoard.append(mergedRow)

    # reverse first, applying shiftingMerging(row), then reverse again"""
    elif direction == 'right':
        reversedBoard = reverse(board)
        mergedBoard = []

        for row in reversedBoard:
            mergedRow = shiftingMerging(row)
            mergedBoard.append(mergedRow)

        newBoard = reverse(mergedBoard)

    # transpose first, apply shiftingMerging(row), then transpose again
    elif direction == 'up':
        transposedBoard = transpose(board)
        mergedBoard = []

        for row in transposedBoard:
            mergedRow = shiftingMerging(row)
            mergedBoard.append(mergedRow)

        newBoard = transpose(mergedBoard)

    # transpose first, reverse second, apply shiftingMerging(row), then reverse and transporse again
    elif direction == 'down':
        transposedBoard = transpose(board)
        reversedBoard = reverse(transposedBoard)
        mergedBoard = []

        for row in reversedBoard:
            mergedRow = shiftingMerging(row)
            mergedBoard.append(mergedRow)

        reversedMergedBoard = reverse(mergedBoard)
        newBoard = transpose(reversedMergedBoard)

    return newBoard

"""
normalizing shiftingMerging for all direction using helper functions transpose() and reverse()
each direction is either reversing the board, transposing, or a combination of both
"""


def gameWon(board):
    for row in board:
        if 32 in row:
            return True
    return False

"""game is won if 2048 is in the board"""


def gameOver(board):

    if moveTiles(board, 'left') != board: # if the previous board is the same
        return False

    if moveTiles(board, 'right') != board:
        return False

    if moveTiles(board, 'up') != board:
        return False

    if moveTiles(board, 'down') != board:
        return False

    return True

"""game is over if there are no available moves"""