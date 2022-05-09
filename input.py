from solver import solve, print_board

# board_example
# [7 8 0 4 0 0 1 2 0],
# [6 0 0 0 7 5 0 0 9],
# [0 0 0 6 0 1 0 7 8],
# [0 0 7 0 4 0 2 6 0],
# [0 0 1 0 5 0 9 3 0],
# [9 0 4 0 6 0 0 0 5],
# [0 7 0 3 0 0 0 1 2],
# [1 2 0 0 0 7 4 0 0],
# [0 4 9 2 0 6 0 0 7]


board = []

print("Welcome to Sudoku Solver!")
print("Please enter the numbers in your Sudoku consecutively with spaces between them")
print("Note: Enter empty boxes in your Sudoku as 0s")


i = 1
while (i <= 9):
    # ask for the numbers in the Suduko in each row.
    n = list(map(int, input("elements of %sst row in Sudoku: " % i).strip().split()))
    if len(n) != 9:
        print("Sorry this is not valid. You must enter 9 numbers. Try again.")
        continue
    board.append(n)
    i += 1

print(" -------------------------------------------------------------- ")
solve(board)
print(" -------------------------------------------------------------- ")
print_board(board)
print(" -------------------------------------------------------------- ")
print("YOUR SUDOKU HAS BEEN SOLVED!")
print(" -------------------------------------------------------------- ")
