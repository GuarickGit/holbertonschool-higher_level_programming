#!/usr/bin/python3

# Importation de argv depuis le module sys
from sys import argv

# Calcul du nombre d'arguments passés (en excluant le nom du script)
n_arguments = len(argv) - 1

# Si aucun argument n'a été passé
if n_arguments == 0:
    print("0 arguments.")
# Si un seul argument a été passé
elif n_arguments == 1:
    print("1 argument:")
# Si plus d'un argument a été passé
elif n_arguments > 1:
    # Affiche le nombre d'arguments suivi de "arguments:"
    print("{} arguments:".format(n_arguments))

# Affiche chaque argument avec son indice, en commençant à 1
for i in range(1, len(argv)):
    # Affiche la position de l'argument et la valeur de l'argument
    print("{}: {}".format(i, argv[i]))
