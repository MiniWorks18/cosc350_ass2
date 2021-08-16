from colorama import Fore, Back
blank = 63 # ASCII value
hoz_bar = "+-------+-------+-------+"
ver_char = "|"
line_col = Fore.CYAN
num_col = Fore.WHITE
bad_col = Back.GREEN+Fore.BLACK

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

def print_sudoku(p): # Print the puzzle to the terminal
    norm = Fore.WHITE+Back.BLACK
    hbar = line_col + hoz_bar + norm
    vchar = line_col + ver_char + norm
    for i in range(len(p)):
        if i % 3 == 0 and i != 0 or i == 0:
            print(hbar)

        for j in range(len(p[0])):
            if j % 3 == 0 and j != 0 or j == 0:
                print(vchar+" ", end="")

            k = bad_col+chr(blank)+norm if p[i][j]==0 else str(p[i][j])
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
    
    if puzzle[i][j] == 0:
        for k in range(len(puzzle)):
            if valid(k, i, j):
                puzzle[i][j] = k
            

def main():
    # print_sudoku(puzzle)
    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):

    # if valid(3, 5, 2):
    #     print("we good")
    # else:
    #     print("we no good")

if __name__ == "__main__":
    main()