#!/usr/bin/python3
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# m = len(matrix) # no of rows
# n = len(matrix[0]) # no of columns

# print("The matrix")
# print(matrix)
# print()

# print(f"First row: {matrix[0]}")
# print(f"First column: {[matrix[i][0] for i in range(m)]}")
# print()

# print("Rows in matrix:")
# for row in matrix:
#     print(row)
# print()

# print("Columns in matrix:")
# for i in range(n):
#     print([matrix[j][i] for j in range(m)])
# print()

# Transposition in single line
# matrix = [[matrix[j][i] for j in range(m)] for i in range(n)]
# print(f"Transposed matrix: {matrix}")
# print()

# for row in matrix:
#     row = row.reverse()
# print(f"Reversed matrix: {matrix}")


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

n = len(matrix)

# In place transposition
for i in range(n): # col
    for j in range(i + 1, n): # row
        print(f"matrix - [{j}][{i}]: {matrix[j][i]}, [{i}][{j}]: {matrix[i][j]}")
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

print(matrix)
# row 0
# row item = 1
# col item = 1
# Swap items
# row 0
# row item = 2
# col item = 4

# row 1
# 

# By transposing:
#   row1 => col1 and col1 => row1
# row1 = matrix[0]
# col1 = [matrix[0][0] matrix[1][0] matrix[2[0]]] OR
#        [matrix[i][0] for i in range(len(matrix) - 1)]

