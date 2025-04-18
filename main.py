from game import BoardState, moveTiles, gameWon, gameOver
from board import placeRandomTile, initBoard, printBoard


def main():

    wasd = { # mapping direction inputs
        'w': 'up',
        'a': 'left',
        's': 'down',
        'd': 'right',
        'u': 'undo'
    }

    while True: # outer loop for playing again

        # initializes the board state
        boardState = BoardState()
        boardState.board = initBoard() # initializes the board
        won = False # tracks win condition, avoiding repetitive prompts
        canUndo = True # tracks if undo is allowed
        canPrint = True # controls whether the board should be printed

        while True: # inner loop for 2048
            if canPrint:
                print("\nCurrent Board:")
                printBoard(boardState.board)

            canPrint = True # resets flag to print the board by default

            if not won and gameWon(boardState.board): # checks if player has won
                print("Congratulations! You've reached 2048!")
                keepPlaying = input("Do you want to keep playing? (yes/no): ").strip().lower()

                if keepPlaying != 'yes':
                    print("You won! Thanks for playing!")
                    break
                won = True # player wants to keep playing so if block doesn't repeat

            if gameOver(boardState.board): # checks if the game is over
                print("Game Over!")
                break

            directionInput = input("Your move: ").strip().lower() # user input

            if directionInput == 'undo': # handles undo input
                if not canUndo:
                    print("You can't undo twice in a row!")
                    canPrint = False # prevents board from being reprinted
                    continue
                if boardState.undo():
                    print("Undo successful!")
                    canUndo = False # disables the flag until a valid move is made
                    canPrint = True # print the board after the first undo
                else:
                    print("No moves to undo!")
                    canPrint = False
                continue

            if directionInput in wasd:
                directionInput = wasd[directionInput]
            elif directionInput not in ['left', 'right', 'up', 'down']:
                print("Invalid input.")
                canPrint = False
                continue # invalid input

            boardState.saveState() # saves the current board state before making a move

            newBoard = moveTiles(boardState.board, directionInput) # creates newBoard after valid move

            if newBoard != boardState.board: # if the board changes
                boardState.board = newBoard
                placeRandomTile(boardState.board) # updates board and add new tiles
                canUndo = True # enables undo after a valid move
            else:
                print("Move not valid. Try a different direction.")
                boardState.previousStates.pop() # removes the saved state if the move was invalid
                canPrint = False

        playAgain = input("Do you want to play again? (yes/no): ").strip().lower()

        if playAgain != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()