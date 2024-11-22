#!/usr/bin/python3
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Reverse matrix
# for row in matrix:
#     row.reverse()

m = len(matrix) # no of rows
n = len(matrix[0]) # no of columns

print("The matrix")
print(matrix)
print()

print(f"First row: {matrix[0]}")
print(f"First column: {[matrix[i][0] for i in range(len(matrix))]}")
print()

print("Rows in matrix:")
for row in matrix:
    print(row)
print()

print("Columns in matrix:")
for i in range(len(matrix)):
    print([matrix[j][i] for j in range(len(matrix))])
print()

matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
print(f"Transposed matrix: {matrix}")


# By transposing:
#   row1 => col1 and col1 => row1
# row1 = matrix[0]
# col1 = [matrix[0][0] matrix[1][0] matrix[2[0]]] OR
#        [matrix[i][0] for i in range(len(matrix) - 1)]

