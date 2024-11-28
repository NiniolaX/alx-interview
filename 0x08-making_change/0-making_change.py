#!/usr/bin/python3
""" Making Change Algorithm

Functions:
    makeChange - Given a pile of different values, calculates the fewest
        number of coins required to meet a given amount total.
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Calculates the fewest number of coins required to make a given total
    amount, given a pile of coins of different values

    Args:
        coins (array of ints): Pile of coins given.
        total (int): Amount to make change of.

    Returns:
        (int): Fewest number of coins required to make total or -1 if total
                cannot be formed with given coins.

    Raises:
        None
    """
    # Initialize array of minimums for all values leading up to total
    minimums = [total + 1] * (total + 1)  # Initialize with arbitrary value

    # Base case
    minimums[0] = 0

    # Iterate over array of minimums to find actual minimum for each index
    for i in range(1, total + 1):
        # Check each coin in pile of coins
        for coin in coins:
            rem = i - coin
            if rem < 0:
                continue

            # Use result from previous calcs to avoid redundant calcs
            curr_min = 1 + minimums[rem]  # 1 represents recently used coin

            # Update minimums with newly found least minimum
            if curr_min < minimums[i]:
                minimums[i] = curr_min

    return minimums[total] if minimums[total] != total + 1 else -1
