#!/usr/bin/python

def new_in_list(my_list, idx, element):
    # Crée une copie de my_list.
    list_copy = list(my_list)
    # Si idx est négatif, return la copie de la liste d'origine.
    if idx < 0:
        return list_copy
    # Si idx est supérieur à la range, return la copie de la liste d'origine.
    elif idx >= len(my_list):
        return list_copy
    # Sinon, modifie l'élément dans la copie de la liste, puis la return.
    else:
        list_copy[idx] = element
        return list_copy
