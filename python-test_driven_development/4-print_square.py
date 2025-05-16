#!/usr/bin/python3

"""
This module provides a function to print a square of '#' characters.
"""


def print_square(size):
    """
    Prints a square made of '#' characters of a given size.

    Args:
    size (int): The size of the square to print. Must be a non-negative integer.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is negative.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
