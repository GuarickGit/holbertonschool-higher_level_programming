#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Compteur pour le nombre d'entiers affichés
    count = 0

    # On parcourt les x premiers éléments de la liste
    for i in range(x):
        try:
            # On essaie d'afficher l'élément comme un entier
            print("{:d}".format(my_list[i]), end=" ")
            # Si l'affichage réussit, on incrémente le compteur
            count += 1

        # Si une exception se produit (ex: type incompatible), on passe
        except (TypeError, ValueError):
            pass

    # On ajoute un retour à la ligne après l'affichage
    print()
    # On retourne le nombre d'entiers affichés
    return count
