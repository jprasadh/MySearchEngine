# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


def all_inputs_valid(puzzle):
    n = len(puzzle)
    for r in puzzle:
        i = 0
        while i < n:
            if not isinstance(r[i], int):
                return False
            i += 1
        if r[0] == r[n-1] and n != 1:
            return False
    for r in puzzle:
        j = 0
        if n != 1:
            if r[j] == r[j + 1]:
                return False
        j += 1

    return True


def check_sudoku(sudoku):
    if not all_inputs_valid(sudoku):
        return False
    n = len(sudoku)
    i = 0
    rowsum = 0
    while i <= n:
        rowsum += i
        i += 1
    # calculates sum of a correct row of the given nxn input, rowsum
    for row in sudoku:
        i = 0
        sumrow = 0
        while i < n:
            sumrow += row[i]
            i += 1
        if sumrow != rowsum:
            return False
    j = 0
    while j < n:
        sumcol = 0
        for k in sudoku:
            sumcol += k[j]
        if sumcol != rowsum:
            return False
        j += 1
    return True


print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False


