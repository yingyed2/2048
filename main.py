from game import BoardState, moveTiles, gameWon, gameOver
from board import placeRandomTile, initBoard, printBoard
from pynput import keyboard

def main():

    wasd = { # mapping direction inputs
        'w': 'up',
        'a': 'left',
        's': 'down',
        'd': 'right',
        'u': 'undo'
    }

    """outer loop for replayability"""
    while True:

        """initializes the board state"""
        boardState = BoardState()
        boardState.board = initBoard() # initializes the board
        won = False # tracks win condition, avoiding repetitive prompts
        canUndo = True # tracks if undo is allowed
        canPrint = True # controls whether the board should be printed
        exitGame = False # tracks if the player wants to exit the game

        """inner loop for 2048"""
        while True:

            if canPrint:
                print("\nCurrent Board:")
                printBoard(boardState.board)

            canPrint = True # resets flag to print the board by default

            if not won and gameWon(boardState.board): # checks if player has won
                print("Congratulations! You've reached 2048!")
                
                while True: # loop until valid input is provided
                    keepPlaying = input("Do you want to keep playing? (yes/no): ").strip().lower()
                    if keepPlaying.startswith('y'):
                        break # exit the loop if input is valid
                    elif keepPlaying.startswith('n'):
                        print("You won! Thanks for playing!")
                        exitGame = True # set flag to exit the game
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")

                if exitGame:
                    break
                won = True # player wants to keep playing so if block doesn't repeat

            if gameOver(boardState.board): # checks if the game is over
                print("Game Over!")
                break

            directionInput = input("Your move: ").strip().lower() # user input

            if directionInput == 'undo' or directionInput == 'u': # handles undo input
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

        if exitGame: # exits the outer loop if the player doesn't want to play again
            break

        while True: # loop until valid input is provided
            playAgain = input("Do you want to play again?: ").strip().lower() # replayability prompt
            if playAgain.startswith('n'):
                print("Thanks for playing!")
                break
            elif playAgain.startswith('y'):
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if playAgain.startswith('n'):
            break
        
"""
main() implements the real-time game loop, allowing players to replay and continue playing;
takes mapped WASD keys as user inputs along with the ability to undo (cannot undo twice in a row)

main() introduces 3 flag variables, canUndo, canPrint, & exitGame to prevent undoing twice in a row
and printing the board after invalid inputs, and fixing a bug with replayability, respectively

initializes board and variables when loop begins, iteratively checking if that game has been won,
allowing for replayability and continuity, and updating and saving the current board after every new valid input
"""


if __name__ == "__main__":
    main()