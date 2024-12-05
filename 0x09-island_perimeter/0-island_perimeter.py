#!/usr/bin/python3
""" Contains a function that calculates the perimeter of an island

Functions:
    - calculate_lonegst_land_strip: Calculates the longest land strip in a
        row or column
    - island_perimeter: Calculates the perimeter of an island
"""


def calculate_longest_land_strip(array: list[int]) -> int:
    """ Calculates the longest land strip in a row/column

    Args:
        array (list of integers): Row/column

    Returns:
        (int): Length of longest land strip

    Raises:
        None
    """
    cell_counter = 0

    # Iterate through row to find longest land strip
    for cell in array:
        if cell == 0 and cell_counter == 0:
            next  # No land cell has been hit
        if cell == 0 and cell_counter != 0:
            break  # Water cell is hit after a land cell/strip
        cell_counter += cell  # Land cell is hit or land script continues

    return cell_counter


def island_perimeter(grid: list[list[int]]) -> int:
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

    len_of_cols = len(grid[0])
    columns = [[row[j] for row in grid] for j in range(len_of_cols)]

    island_width = 0
    island_length = 0

    # Calculate island width
    for row in grid:
        widest_land_space = calculate_longest_land_strip(row)

        # Update island_width variable with longest row
        if island_width < widest_land_space:
            island_width = widest_land_space

    # Calculate island length
    for col in columns:
        longest_land_space = calculate_longest_land_strip(col)

        if island_length < longest_land_space:
            island_length = longest_land_space

    perimeter = 2 * (island_length + island_width)
    return perimeter
