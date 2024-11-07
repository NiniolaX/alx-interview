#!/usr/bin/python3
""" This script solves and prints all solution to the N-Queens Problem

Functions:
    main: Main function to execute the N-Queens solver.
        Args: None
        Returns: None

    is_safe_position: Checks if a position is safe to place a queen.
        Args:
            queens (list of ints): Coordinates/positions of placed queens
            row (int): Row to check
            col (int): column to check
        Returns: bool

    solve_nqueens: Solves the N-Queens problem using backtracking.
        Args:
            n (int): board_size
        Returns(list of list of lists of integers): All possible solutions to
            for specified board size
"""
import sys


def is_safe_position(queens: list[list[int]], row: int, col: int) -> bool:
    """ Checks if a postion is safe to place a queen """
    for r, c in queens:
        # Checks that no queen exists on that row or column or diagonal
        if r == row or c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n: int) -> list[list[list[int]]]:
    """ Returns all possible solutions to the N-Queens problem """
    solutions = []

    def backtrack(queens: list[list[int]], row: int) -> None:
        """
        Removes last placed queen from her previous position on board to
        to next safe position.
        """
        if row == n:
            solutions.append(queens[:])
            return

        for col in range(n):
            if is_safe_position(queens, row, col):
                queens.append([row, col])  # Place queen
                backtrack(queens, row + 1)  # Recurse to next row
                queens.pop()  # Backtrack (remove queen)

    # Start backtracking from first row and empty queens list
    backtrack([], 0)
    return solutions


def main():
    """ Main function to execute N-Queens solver """
    # Validate number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate board size
    board_size = sys.argv[1]
    try:
        board_size = int(board_size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve N-Queens problem for given board size
    solutions = solve_nqueens(board_size)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
