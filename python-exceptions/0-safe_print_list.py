#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Compteur du nombre d'éléments réellement imprimés
    count = 0
    for i in range(x):  # On essaie d'imprimer x éléments
        try:
            # On imprime l'élément sans retour à la ligne
            print(my_list[i], end="")
            # Si l'impression réussit, on incrémente le compteur
            count += 1
        except:
            # Si l'élément n'existe pas (IndexError), on arrête la boucle
            break
    # On imprime un retour à la ligne après tous les éléments
    print()
    # On retourne le nombre réel d'éléments imprimés
    return count
