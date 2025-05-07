#!/usr/bin/python3

# Importation du module argv depuis le package sys
from sys import argv

# Vérifie si le script est exécuté directement (et non importé)
if __name__ == "__main__":
    # Calcul du nombre d'arguments passés (en excluant le nom du script)
    n_arguments = len(argv) - 1

    # Si aucun argument n'est passé, afficher 0 arguments
    if n_arguments == 0:
        print("0 arguments.")

    # Si un seul argument est passé, afficher 1 argument
    elif n_arguments == 1:
        print("1 argument:")

    # Si plus d'un argument est passé, afficher le nombre d'arguments
    elif n_arguments > 1:
        print("{} arguments:".format(n_arguments))

    # Parcours de tous les arguments (start à 1, sans le nom du script)
    for i in range(1, len(argv)):
        # Affiche l'indice de l'argument et la valeur de l'argument
        print("{}: {}".format(i, argv[i]))
