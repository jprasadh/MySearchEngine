# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        next_row = [1]
        output = triangle(n-1)
        prev_row = output[-1]
        for i in range(len(prev_row) - 1):
            next_row.append(prev_row[i] + prev_row[i + 1])
        next_row.append(1)
        output.append(next_row)
    return output


def next_row(row):
    nextrow = []
    prev = 0
    for num in row:
        nextrow.append(num + prev)
        prev = num
    nextrow.append(prev)
    return nextrow


def triangle_iter(n):
    output = []
    row = [1]
    for unused in range(0, n):
        output.append(row)
        row = next_row(row)
    return output


# For example:

# print triangle(0)
# >>> []

# print triangle(1)
# >>> [[1]]

print(triangle(2))
# >> [[1], [1, 1]]

print(triangle(3))
# >>> [[1], [1, 1], [1, 2, 1]]

print(triangle_iter(6))
# >>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
