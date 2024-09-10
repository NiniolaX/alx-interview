#!/usr/bin/python3
"""
This module contains a function that returns the minimum number of operations
needed to result in a file having exactly nH characters, wherem
    - file originally has only 1H character,
    - the only operations that can be performed on the file are 'Copy All'
        and 'Paste'.
Functions:
    minOperations: Computes the minimum number of operations to result in a
    file having nH characters.
"""


def minOperations(n: int) -> int:
    """Computes the minimum number of operations to result in a file
    having nH characters
    """
    if n < 1:
        # No operations needed since file already has 1H characters
        return 0

    operations = 0
    divisor = 2

    # Using prime factorization technique
    while n != 1:
        # Continually divide by divisor until n is no longer divisible by it
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1

    return operations
