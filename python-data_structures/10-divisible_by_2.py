#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    # Initialise une nouvelle liste vide pour stocker les résultats
    new_list = []
    # Parcourt chaque élément de la liste donnée
    for number in my_list:
        # Vérifie si le nombre est divisible par 2
        if number % 2 == 0:
            # Ajoute True à la nouvelle liste
            new_list.append(True)

        # Sinon, ajoute False à la nouvelle liste
        else:
            new_list.append(False)
    # Retourne la liste complète des booléens
    return new_list
