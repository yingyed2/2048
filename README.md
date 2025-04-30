Project: Recreating the popular game 2048 as part of our final project for ECE-160 Spring 2025

Description: This is a python implementation of the classic 2048 game, where players combine tiles, of powers of 2,to reach the number 2048. The game is played on a 4x4 grid, and tiles move in response to arrow key inputs.

Features: 
- tile meging
- arrow key controls for movement
- score tracking (?)
- game over detection
- terminal-based

Controls:
- Arrow keys or WASD keys 
- Tiles merge when two tiles of the same nuumber collide, doubling their value.
- New tiles (usually 2 or 4) appear in an empty spot after every move.

Rules:
- You can slide tiles in four directions: Up, Down, Left, Right.
- When two tiles with the same number touch, they merge into one tile of their combined value.
- Each move spawns a new tile (2 or 4) at a random empty position.
- The game ends when there are no possible moves left (no empty spaces and no adjacent tiles that can merge).
- The score increases with every merge.

To compile and run (version dependent, but file should be main.py):
python3.12 main.py 

After a game where the user lost, the final output might look like this:
---------------------
|  2 |  4 |  8 | 16 |
---------------------
|  4 |  8 | 16 | 32 |
---------------------
|  8 | 16 | 32 | 64 |
---------------------
| 16 | 32 | 64 | 128|
---------------------

Game Over! Final Score: 512

After a game where the user won, the final output might look like this: 
---------------------
|  2 |  4 |  8 | 16 |
---------------------
| 32 | 64 | 128| 256|
---------------------
| 512|1024|2048|  4 |
---------------------
|  8 | 16 | 32 | 64 |
----------------------

🎉 Congratulations! You reached 2048! 🎉
🏆 You Win! 🏆

