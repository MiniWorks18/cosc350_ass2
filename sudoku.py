from colorama import Fore, Back
import time
import pdb
blank = 63 # ASCII value
hoz_bar = "+-------+-------+-------+"
ver_char = "|"
line_col = Fore.CYAN
num_col = Fore.WHITE
unknown_col = Back.GREEN+Fore.BLACK
bad_col = Fore.RED

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

correct_puzzle = [
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

def print_sudoku(): # Print the puzzle to the terminal
    p = puzzle
    norm = Fore.WHITE+Back.BLACK
    hbar = line_col + hoz_bar + norm
    vchar = line_col + ver_char + norm
    for i in range(len(p)):
        if i % 3 == 0 and i != 0 or i == 0:
            print(hbar)

        for j in range(len(p[0])):
            if j % 3 == 0 and j != 0 or j == 0:
                print(vchar+" ", end="")
            if p[i][j]==0:
                k = unknown_col+chr(blank)+norm 
            else: 
                k = str(p[i][j])
                if k != str(correct_puzzle[i][j]):
                    k = bad_col+k
            if j == 8:
                print(num_col + k + " " +vchar)
            else:
                print(num_col + k + " ", end="")
    print(hbar)

# Checks that a particular int can be placed at puzzle[i][j]
def valid(x, i, j):
    row = puzzle[i] # Fetch the row
    col = []
    for k in range(len(puzzle[0])): # Fetch the collum
        col.append(puzzle[k][j])
    
    block = []
    block_x = i // 3
    block_y = j // 3
    for k in range(len(puzzle[0])): # Fetch the block that the position is in
        for e in range(len(puzzle)):
            if k // 3 == block_x and e // 3 == block_y:
                block.append(puzzle[k][e])
    return x not in row and x not in col and x not in block

def solve(i, j):
    if i == len(puzzle):
        j += 1
        i = 0
        if j == len(puzzle[0]):
            return True
        # print_sudoku()
        # input("New collum complete! Enter to continue...")
    print_sudoku()
    time.sleep(0.3)
    # print("i = ", i)
    # print("j = ", j)
    if puzzle[i][j] == 0:
        for k in range(1,1+len(puzzle)):
            if valid(k, i, j):
                puzzle[i][j] = k
                if solve(i+1, j):
                    return True
                else:
                    puzzle[i][j] = 0

    elif solve(i+1, j):
        return True
    else:
        return False
            
            

def main():
    print("This program will use traversal backtracking to solve the following sudoku:")
    print_sudoku()
    input("Press enter to begin...")
    solve(0,0)
    print_sudoku()
    # if valid(3, 5, 2):
    #     print("we good")
    # else:
    #     print("we no good")

if __name__ == "__main__":
    main()