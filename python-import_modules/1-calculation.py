#!/usr/bin/python3

# Importe les fonctions add, sub, mul et div depuis le module calculator_1
from calculator_1 import add, sub, mul, div
a = 10 # Initialise la variable a avec la valeur 10
b = 5 # Initialise la variable b avec la valeur 5

# Exécute ce bloc uniquement si le script est lancé directement
if __name__ == "__main__":
    # Affiche le résultat de l'addition
    print("{} + {} = {}".format(a, b, add(a, b)))
    # Affiche le résultat de la soustraction
    print("{} - {} = {}".format(a, b, sub(a, b)))
    # Affiche le résultat de la multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))
    # Affiche le résultat de la division
    print("{} / {} = {}".format(a, b, div(a, b)))
