#!/usr/bin/python3

"""
This module provides a function that prints a full name,
constructed from a first and an optional last name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a full name in the format 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str): The optional last name to print (default is "").

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = " ".join(part for part in [first_name, last_name] if part)

    print(f"My name is{name and ' ' + name}")
