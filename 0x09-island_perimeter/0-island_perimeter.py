#!/usr/bin/python3
""" Contains a function that calculates the perimeter of an island

Functions:
    - calculate_lonegst_land_strip: Calculates the longest land strip in a
        row or column
    - island_perimeter: Calculates the perimeter of an island
"""


def island_perimeter(grid) -> int:
    """ Calculates the perimeter of an island represeted on a grid of integers

    Args:
        grid(list of list of integers): Grid

    Returns:
        (int): Perimeter of the island

    Raises:
        None
    """
    if not grid:
        return 0

    len_rows = len(grid)
    len_cols = len(grid[0])

    perimeter = 0

    for i in range(len_rows):
        for j in range(len_cols):
            if grid[i][j] == 1:  # Land cell
                perimeter += 4  # Start with 4 sides

                # Check cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1  # Subtract 1 for shared edge

                # Check cell to the right
                if j < len_cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1  # Subtract 1 for shared edge

                # Check cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1  # Subtract 1 for shared edge

                # Check cell below
                if i < len_rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1  # Subtract 1 for shared edge

    return perimeter
