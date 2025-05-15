#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Initialise un compteur pour le nombre d'entiers affichés
    count = 0

    # Tente d'afficher les x premiers éléments de la liste
    for i in range(x):
        try:
            # Affiche l'élément s'il peut être formaté en entier
            print("{:d}".format(my_list[i]), end="")
            # Incrémente le compteur si l'affichage réussit
            count += 1
        # Ignore les éléments qui ne sont pas des entiers
        except (TypeError, ValueError):
            continue

    # Ajoute un saut de ligne après l'affichage
    print()

    # Retourne le nombre d'entiers effectivement affichés
    return count
