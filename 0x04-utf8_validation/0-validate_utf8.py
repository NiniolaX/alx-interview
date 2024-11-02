#!/usr/bin/python3
"""
This module contains a function "validUTF8" that checks if a given data set
represents a valid UTF-8 encoding.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Checks if a given data set represents a valid UTF-8 encoding.

    Args:
        (list of integers): Dataset to validate

    Returns:
        (bool): True if valid UTF-8 encoding, False if otherwise
    """
    # Number of bytes left to be checked
    num_of_bytes = 0  # Set to 0 to indicate start of a new character

    for char in data:
        # Extract the least significant bytes of the character
        lsb = char & 0xFF

        if num_of_bytes == 0:
            if (lsb >> 5) == 0b110:
                num_of_bytes = 1  # Bytes left to check for 2-byte integer
            elif (lsb >> 4) == 0b1110:
                num_of_bytes = 2  # Bytes left to check for 3-byte integer
            elif (lsb >> 3) == 0b11110:
                num_of_bytes = 3  # Bytes left to check for 4-byte integer
            elif (lsb >> 7):
                # MSB for 1-byte characters should be 0 not 1
                return False

        else:
            if (lsb >> 6) != 0b10:
                return False
            num_of_bytes -= 1

        return num_of_bytes == 0  # True if all bytes were correctly processed
