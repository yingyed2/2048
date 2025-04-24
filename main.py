from board import BoardState, reset, placeRandomTile, initBoard, printBoard
from game import moveTiles, gameWon, gameOver
from pynput import keyboard # keyboard listening
import os
import sys
import termios


def clearBufferedInputs():
    if os.name == 'posix': # macOS
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

"""
clears any buffered input in the terminal
fixing a previous bug with keyboard listening
"""


def main():

    wasd = { # mapping direction inputs
        'w': 'up',
        'a': 'left',
        's': 'down',
        'd': 'right',
        'u': 'undo',
        'r': 'reset'
    }

    listener = None # initialize the listener variable

    try:

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

                """replay conditional"""
                if not won and gameWon(boardState.board): # checks if player has won
                    print("Congratulations! You've reached 2048!")
                    
                    while True: # loop until valid input is provided
                        keepPlaying = input("Do you want to keep playing?").strip().lower() # normalize input to lowercase
                        if keepPlaying.startswith('y'):
                            break # exit the loop if input is valid
                        elif keepPlaying.startswith('n'):
                            print("You won! Thanks for playing!")
                            exitGame = True
                            break
                        else:
                            print("Invalid input.")

                    if exitGame:
                        break
                    won = True # player wants to keep playing so if block doesn't repeat

                if gameOver(boardState.board): # checks if the game is over
                    print("Game Over!")
                    break

                print("Your move:")

                # wait for a valid key press using pynput
                directionInput = None

                """helper function to create key listening"""
                def on_press(key):
                    nonlocal directionInput
                    try:
                        char = key.char.lower() # normalize input to lowercase
                        if char in wasd:
                            directionInput = char
                            return False # stop listener
                    except AttributeError:
                        pass

                listener = keyboard.Listener(on_press=on_press, suppress=True)
                listener.start()
                listener.join() # wait for the listener to stop

                """undo conditional"""
                if directionInput == 'u': # handles undo input
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

                """reset conditional"""
                if directionInput == 'r': # handles reset input
                    reset(boardState)
                    canUndo = True # enables undo after reset
                    canPrint = True # print the board after reset
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

            """replay loop"""
            while True: # loop until valid input is provided
                playAgain = input("Do you want to play again?: ").strip().lower()
                if playAgain.startswith('n'):
                    print("Thanks for playing!")
                    exitGame = True
                    break
                elif playAgain.startswith('y'):
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            if exitGame:
                break

    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting gracefully...")
    finally:
        if listener and listener.running:
            listener.stop() # ensures the listener is stopped
        clearBufferedInputs() # clear any buffered input

"""
main() implements the real-time game loop, allowing players to replay and continue playing;
takes mapped WASD keys as user inputs along with the ability to undo (cannot undo twice in a row)

main() introduces 3 flag variables, canUndo, canPrint, & exitGame to prevent undoing twice in a row
and printing the board after invalid inputs, and fixing a bug with replayability, respectively

initializes board and variables when loop begins, iteratively checking if that game has been won,
allowing for replayability and continuity, and updating and saving the current board after every new valid input

implements keyboard listening features and fixing its bugs through importing keyboard from pynput,
& importing os, sys, and terminal
"""


if __name__ == "__main__":
    main()