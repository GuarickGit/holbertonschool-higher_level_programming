#!/usr/bin/python3

def safe_print_division(a, b):

    # On initialise result à None par défaut
    result = None

    # On essaie de faire la division
    try:
        result = a / b
    # Si une division par zéro se produit, on garde result à None
    except ZeroDivisionError:
        result = None
    # Ce bloc s'exécute toujours, que l'exception ait eu lieu ou non
    finally:
        print("Inside result: {}".format(result))

    # On retourne le résultat (None si erreur, ou le résultat de la division)
    return result
