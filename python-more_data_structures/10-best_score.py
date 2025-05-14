#!/usr/bin/python3

def best_score(a_dictionary):
    # Si le dictionnaire est vide ou None, retourner None
    if not a_dictionary:
        return None

    # Trouver la valeur maximale parmi toutes les valeurs du dictionnaire
    max_value = max(a_dictionary.values())

    # Parcourir chaque clé du dictionnaire
    for key in a_dictionary:
        # Si la valeur associée à cette clé est égale à la valeur maximale
        if a_dictionary[key] == max_value:
            # Retourner cette clé
            return key
