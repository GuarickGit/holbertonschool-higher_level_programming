#!/usr/bin/python3
def islower(c):

    # Vérifie si le code ASCII du caractère (c) est entre 97 ('a') et 122 ('z')
    # ord() : Prend un caractère, retourne son code ASCII (Decimal)
    if ord(c) >= 97 and ord(c) <= 122:
        # Si oui, c'est une lettre minuscule, donc retourne True.
        return True
    else:
        # Sinon, ce n'est pas une minuscule, donc retourne False.
        return False
