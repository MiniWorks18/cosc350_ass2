from colorama import Fore, Back
import time
import pdb
import random
blank = 63 # ASCII value of blank spaces
size = 9 # Width/height of sudoku puzzle
speed = 0.2 # Time in seconds between iterations
puzzle_generator = False # Toggle random sudoku generator
difficulty = 20 # Lower = more difficult
hoz_bar = "+-------+-------+-------+"
ver_char = "|"
line_col = Fore.CYAN # Border colour
num_col = Fore.WHITE # Colour of numbers
unknown_col = Back.GREEN+Fore.BLACK # Colour of unknown characters
bad_col = Fore.RED # Colour of misplaced characters
puzzle = [[0 for i in range(size)] for i in range(size)]
solved_puzzle = [[0 for i in range(size)] for i in range(size)]

# Print the puzzle to the terminal
#   p - Puzzle to print
def print_sudoku(p):
    # Colour formating
    norm = Fore.WHITE+Back.BLACK
    hbar = line_col + hoz_bar + norm
    vchar = line_col + ver_char + norm
    for i in range(size): # For each collum
        if i % 3 == 0 and i != 0 or i == 0:
            print(hbar)
        for j in range(size): # For each cell in collum
            if j % 3 == 0 and j != 0 or j == 0: # Place vertical characters
                print(vchar+" ", end="")
            if p[i][j]==0: # Place unknown characters
                k = unknown_col+chr(blank)+norm 
            else: # Place known numbers
                k = str(p[i][j])
                if k != str(solved_puzzle[i][j]) and not puzzle_generator:
                    k = bad_col+k
            if j == 8:
                print(num_col + k + " " +vchar)
            else:
                print(num_col + k + " ", end="")
    print(hbar)

# Checks that a particular int can be placed at puzzle[i][j]
#   puzzle - Puzzle to check validation on
#   new - The new number to place
#   x - The cell position
#   y - The collumn
def valid(puzzle, new, x, y):
    row = puzzle[x] # Fetch the row
    col = []
    block = []
    block_x = x // 3
    block_y = y // 3
    for k in range(size): # Fetch the collum
        col.append(puzzle[k][y])
    for k in range(size): # Fetch the block that the position is in
        for e in range(size):
            if k // 3 == block_x and e // 3 == block_y:
                block.append(puzzle[k][e])
    return new not in row and new not in col and new not in block

# Recursive solve function, this will call itself for each cell until solved
#   int[][] puzzle - The puzzle to solve
#   int i - The position of the cell
#   int j - The position of the collum
#   bool verbose - Print progress or not
def solve(puzzle, i, j, verbose):
    if i == size: # If end of collum, move to next collum
        j += 1
        i = 0
        if j == size: # If last collum, return success
            return True
    if puzzle[i][j] == 0: # If cell needs filling
        if (verbose):
            print_sudoku(puzzle)
            time.sleep(speed)
        # Random sequencing (useful for generating sudokus)
        seq = list(range(1, 1+size))
        random.shuffle(seq)
        for k in seq: # Recursively attempt each number from 1 to size
            if valid(puzzle, k, i, j):
                puzzle[i][j] = k
                if solve(puzzle, i+1, j, verbose):
                    return True
                else:
                    puzzle[i][j] = 0
    else:
        return solve(puzzle, i+1, j, verbose)

# Either provides hard coded sudoku (per assignment requirements)
# or generates a new sudoku and attempts to quickly solve it before
# showing the user how it solves them
def fetch_puzzle():
    global puzzle
    global solved_puzzle
    if puzzle_generator:
        print("Generating...")
        good_generation = False
        solved_puzzle = [[0 for i in range(size)] for i in range(size)]
        for i in range(difficulty): # Attempt to place new num per difficulty
            new = random.randrange(0,9)
            x = random.randrange(0,9)
            y = random.randrange(0,9)
            if valid(solved_puzzle, new, x, y):
                solved_puzzle[x][y] = new
                puzzle[x][y] = new
        solve(solved_puzzle,0,0,False)
    else: # Return hard coded assignment sudoku
        puzzle = [
            [9,0,0, 1,7,0, 4,0,2],
            [1,6,0, 0,4,0, 0,9,5],
            [0,0,8, 0,0,3, 0,0,0],

            [0,1,0, 9,0,0, 5,7,3],
            [0,4,0, 0,0,0, 0,2,0],
            [5,8,9, 0,0,7, 0,1,0],

            [0,0,0, 4,0,0, 7,0,0],
            [6,7,0, 0,2,0, 0,5,8],
            [3,0,1, 0,5,8, 0,0,6]
            ]
        # Puzzle solution, used for error checking in terminal graphic
        solved_puzzle = [
            [9,3,5, 1,7,6, 4,8,2],
            [1,6,7, 8,4,2, 3,9,5],
            [4,2,8, 5,9,3, 1,6,7],

            [2,1,6, 9,8,4, 5,7,3],
            [7,4,3, 6,1,5, 8,2,9],
            [5,8,9, 2,3,7, 6,1,4],

            [8,5,2, 4,6,9, 7,3,1],
            [6,7,4, 3,2,1, 9,5,8],
            [3,9,1, 7,5,8, 2,4,6]
            ]

# Main function orchestrating the process
def main():
    print("This program will use Depth First Search to solve the " 
    +"following sudoku:")
    fetch_puzzle()
    print_sudoku(puzzle)

    # Initial information
    print("Author: Tully McDonald")
    print("Purpose:")
    print("The purpose of this program is to solve a sudoku puzzle "
    +"using an AI search algorithm called Depth First Search (DFS) "
    +"which is a type of backtracking search.")
    print("\nThe program recursively calls a solve function to explore "
    +"all posibilities while the puzzle is still legal")
    print("\nIf the function cannot find a suitable digit for a specific cell "
    +"then it will assume it's made a mistake and will backtrack to try a "
    +"different digit in a previous cell")
    print("\nAdditional feature:")
    print("There is a puzzle generator embeded within the source code, switch "
    +"puzzle_generator to True to use this feature")
    input("\n\nPress enter to begin...")

    # Attempt to solve
    if solve(puzzle,0,0, True):
        print("\n\n\nSudoku solved! Solution below:")
    else:
        print("Could not solve sudoku")
    print_sudoku(puzzle)

if __name__ == "__main__":
    main()