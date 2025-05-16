#!/usr/bin/python3
"""
This module provides a function that adds two integers.

The function accepts integers and floats, converts floats to integers,
and raises a TypeError if inputs are not valid.
"""


def add_integer(a, b=98):
    """
    Adds two numbers (integers or floats) and returns their sum as an integer.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        int: The sum of a and b, after converting floats to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
