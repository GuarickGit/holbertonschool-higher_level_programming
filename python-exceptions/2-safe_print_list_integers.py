#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Initialise un compteur pour le nombre d'entiers imprimés
    count = 0

    # Parcourt les x premiers éléments ou jusqu'à la fin de la liste
    # (le plus petit des deux)
    for i in range(min(x, len(my_list))):
        try:
            # Tente d'imprimer l'élément en tant qu'entier (format {:d})
            print("{:d}".format(my_list[i]), end=" ")
            # Incrémente le compteur si l'impression réussit
            count += 1

        # Ignore les éléments qui ne sont pas des entiers
        except (TypeError, ValueError):
            pass

    # Ajoute un saut de ligne après l'affichage
    print()
    # Retourne le nombre d'entiers imprimés
    return count
