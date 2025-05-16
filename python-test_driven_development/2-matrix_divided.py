def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) containing
            only integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
            if the rows are not of the same size or empty, or if div is not
            a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with all values divided by div,
        rounded to 2 decimal places.
    """

    # Vérifie que matrix est une liste non vide
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Vérifie que chaque ligne est une liste non vide
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Vérifie que tous les éléments sont des int ou float
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )

    # Vérifie que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Vérifie que div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérifie que div n’est pas égal à zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création d’une nouvelle matrice avec division et arrondi
    new_matrix = [
        [round(item / div, 2) for item in row] for row in matrix
    ]

    return new_matrix
