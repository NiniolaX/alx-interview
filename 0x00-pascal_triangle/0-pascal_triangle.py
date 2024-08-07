#!/usr/bin/python3
"""
Returns a list of integers representing the Pascal's triangle
"""


def pascal_triangle(n):
    """ Fnction returns a list of integers representing Pascal's Triangle
    Args:
        n(int): Number of triangle rows to print
    Return:
        list of lists: List of integers of triangle organized into rows
    """
    if n <= 0:
        return []

    result = []  # Define triangle (array of arrays)

    for i in range(n):
        row = [1]  # First element is always 1
        if i > 0:
            for j in range(1, i):
                element = (result[i-1][j-1] + result[i-1][j])
                row.append(element)
            row.append(1)  # Last element is always 1
        result.append(row)  # Append row (array) to triangle

    return result

# Notes:
# Inner loop: Used the values in earlier rows saved in result rather than
#     formulas involving factorials for efficiency.
# Line 11: Started iteration from 2nd element (index 1) and ended at 2nd to
#     the last element (index i) since first & last elements will always be 1.
# i represents current row, max possible is n
# j represents current column, max possible is n+1
