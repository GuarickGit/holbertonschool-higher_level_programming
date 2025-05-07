#!/usr/bin/python3

# Importe la fonction add depuis le module add_0
from add_0 import add
a = 1 # Déclare et initialise la variable a avec la valeur 1
b = 2 # Déclare et initialise la variable b avec la valeur 2

# Vérifie si ce script est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    # Affiche le résultat de l'addition de a et b en utilisant la fonction add
    print("{} + {} = {}".format(a, b, add(a, b)))
