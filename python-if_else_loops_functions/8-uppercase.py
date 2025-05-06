#!/usr/bin/python3
def uppercase(str):
    # Parcourt chaque caractère de la chaîne.
    for character in str:
        # Si le caractère est une lettre minuscule (a à z).
        if ord(character) >= 97 and ord(character) <= 122:
            # On le convertit en majuscule (décalage de -32 entre 'a' et 'A').
            upper_character = chr(ord(character) - 32)
        else:
            # Sinon, on le garde tel quel.
            upper_character = character
        # Affiche le caractère, sans retour à la ligne. (end="").
        print("{}".format(upper_character), end="")
    # Saut de ligne à la fin de l'affichage
    # ATTENTION ! print("\n") saute 2x à la ligne.
    print()
