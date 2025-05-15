#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Tente d'afficher la valeur comme un entier
        # Si value n'est pas un entier, format() lèvera une TypeError
        print("{:d}".format(value))
        return True
    except TypeError:
        # Si une erreur de type est levée (ex : string, etc), on retourne False
        return False
