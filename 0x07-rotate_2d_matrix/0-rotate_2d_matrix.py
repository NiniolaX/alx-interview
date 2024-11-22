#!/usr/bin/python3
""" Contains a function that rotates a 3D matrix.

Functions:
    rotate_2d_matrix: Rotates an n X n matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """ Rotates an nXn matrix 90 degrees clockwise

    Args:
        (list of list): Matrix

    Returns:
        None
    """
    if not matrix:
        return

    n = len(matrix)

    for i in range(n):  # col
        for j in range(i + 1, n):  # row
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
