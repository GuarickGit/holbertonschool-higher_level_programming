#!/usr/bin/python3
"""
Module qui génère le triangle de Pascal jusqu'à une profondeur donnée.
Contient une seule fonction : pascal_triangle(n).
"""

def pascal_triangle(n):
    """
    Génère le triangle de Pascal jusqu'à la ligne n (incluse).

    Le triangle de Pascal est une structure mathématique où chaque nombre
    est la somme des deux nombres situés juste au-dessus de lui.

    Args:
        n (int): Le nombre de lignes du triangle à générer.

    Returns:
        list: Une liste de listes d'entiers représentant le triangle.
              Chaque sous-liste correspond à une ligne du triangle.
              Retourne une liste vide si n <= 0.
    """

    # Si n est inférieur ou égal à 0, on retourne une liste vide
    if n <= 0:
        return []

    # Initialisation du triangle avec la première ligne : [1]
    triangle = [[1]]

    # Génération des lignes suivantes jusqu'à en avoir n
    while len(triangle) < n:

        # Dernière ligne ajoutée au triangle
        last_row = triangle[-1]
        # Nouvelle ligne à construire, commence toujours par 1
        new_row = [1]

        # Calcul des valeurs intermédiaires : somme de deux éléments voisins
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        # Chaque ligne se termine toujours par 1
        new_row.append(1)

        # Ajout de la ligne construite au triangle
        triangle.append(new_row)

    # Une fois les n lignes construites, on retourne le triangle
    return triangle
