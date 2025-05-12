#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Si idx est négatif, return la liste sans rien faire.
    if idx < 0:
        return my_list
    # Si idx est supérieur à la range, return la liste sans rien faire.
    elif idx >= len(my_list):
        return my_list
    # Sinon, remplace l'élement à la position idx, puis retourne la liste.
    else:
        my_list[idx] = element
        return my_list
