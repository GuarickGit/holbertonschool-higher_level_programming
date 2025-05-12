#!/usr/bin/python3

def no_c(my_string):
    # Déclaration de la variable qui contiendra la nouvelle string.
    new_string = ""
    # Boucle sur tous les caractères de my_string.
    for letter in my_string:
        # Si letter n'est pas égale à 'C' et'c':
        if letter != 'C' and letter != 'c':
            # Alors on ajoute la lettre à la nouvelle string.
            new_string += letter
    # On return la nouvelle string.
    return new_string
