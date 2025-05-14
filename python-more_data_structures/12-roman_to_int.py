#!/usr/bin/python3

def roman_to_int(roman_string):
    # Dictionnaire associant chaque lettre romaine à sa valeur
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    result = 0  # Résultat final à retourner
    last_value = 0  # Dernière valeur rencontrée, pour gérer les soustractions

    # Vérifie que l'entrée est une chaîne non nulle
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    # Parcourt la chaîne de droite à gauche
    for char in reversed(roman_string):
        value = roman_dict[char]  # Récupère la valeur de la lettre romaine

        # Si la valeur actuelle est inférieure à la précédente, on la soustrait
        if value < last_value:
            result -= value
        else:
            # Sinon, on l'ajoute
            result += value

        # Met à jour la dernière valeur pour la prochaine itération
        last_value = value

    # Retourne le résultat final
    return result
