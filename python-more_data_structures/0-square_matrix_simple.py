#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Nouvelle matrice qui contiendra les valeurs au carré
    new_matrix = []
    # Pour chaque ligne de matrix
    for row in matrix:
        # Nouvelle ligne pour stocker les carrés de la ligne actuelle
        square_line = []
        # Pour chaque élément de row
        for num in row:
            # On élève chaque nombre au carré et on l’ajoute à la ligne
            square_line.append(num ** 2)
        # On ajoute la ligne complète à la nouvelle matrice
        new_matrix.append(square_line)
    # On retourne la nouvelle matrice avec toutes les valeurs au carré
    return new_matrix
