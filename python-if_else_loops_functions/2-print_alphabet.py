#!/usr/bin/python3

# Boucle de 'a' à 'z' (97 à 123 en ASCII).
for letter in range(97, 123):
    # Print le character actuel dans letter, sans saut à la ligne.
    print("{}".format(chr(letter)), end="")
