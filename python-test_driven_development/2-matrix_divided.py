#!/usr/bin/python3

"""
This module provides a function that divides all elements of a matrix
by a given number, with validation and rounding to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) containing
            only integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
            if the rows are not of the same size, or if div is not
            a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with all values divided by div,
        rounded to 2 decimal places.
    """

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            result = round(item / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
