#!/usr/bin/python3

# Boucle de 'a' à 'z' (97 à 123 en ASCII).
for letter in range(97, 123):
    # Si letter n'est pas égale à 'e' ET 'q'.
    if letter != 101 and letter != 113:
        # Print le character actuel dans letter, sans saut à la ligne.
        # chr(letter) pour ASCII | end="" pour pas de retour à la ligne.
        print("{}".format(chr(letter)), end="")
