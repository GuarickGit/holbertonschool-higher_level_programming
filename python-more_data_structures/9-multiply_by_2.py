#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # On crée un nouveau dictionnaire vide pour stocker les résultats
    new_dictionary = {}
    # On parcourt chaque paire clé/valeur du dictionnaire original
    for key, value in a_dictionary.items():
        # On multiplie la valeur par 2 et on l'associe à la même clé
        # dans le nouveau dictionnaire
        new_dictionary[key] = value * 2

    # On retourne le nouveau dictionnaire une fois toutes les paires modifiées
    return new_dictionary
