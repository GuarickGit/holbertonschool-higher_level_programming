#!/usr/bin/python3

# Importation du module argv depuis le package sys
from sys import argv

# Vérifie si le script est exécuté directement (et non importé)
if __name__ == "__main__":
    # Initialisation de la variable n_arguments à 0 pour commencer l'addition
    n_arguments = 0
    # Parcourt les arguments à partir de argv[1], sans le nom du script
    for args in argv[1:]:
        # Convertit chaque argument en entier et l'ajoute à n_arguments
        n_arguments += int(args)
    # Affiche la somme de tous les arguments
    print(n_arguments)
