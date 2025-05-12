#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Boucle sur les lignes de matrix.
    for row in matrix:
        # Boucle sur les caractères de la ligne.
        for i in range(len(row)):
            # Si i est égale à la length de row - 1.
            if i == len(row) - 1:
                # Print le caractère actuel de la ligne, sans espace.
                print("{:d}".format(row[i]), end="")
            else:
                # Print le caractère actuel de la ligne, avec espace.
                print("{:d}".format(row[i]), end=" ")
        # Print un retour à la ligne.
        print()
