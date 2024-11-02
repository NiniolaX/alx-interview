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
        # Extract the least significant bits of character
        lsb = char & 0xFF

        # Validate pattern of MSB
        if num_of_bytes == 0:
            if (lsb >> 5) == 0b110:
                num_of_bytes = 1  # For 2-byte integer
            elif (lsb >> 4) == 0b1110:
                num_of_bytes = 2  # For 3-byte integer
            elif (lsb >> 3) == 0b11110:
                num_of_bytes = 3  # For 4-byte integer
            elif (lsb >> 7) == 0b0:
                continue  # For 1-byte integer
            else:
                return False

        # Validate continuation bytes (Should be 10000000, otherwise invalid)
        else:
            if (lsb >> 6) != 0b10:
                return False
            num_of_bytes -= 1

    return num_of_bytes == 0  # True if all bytes were correctly processed
