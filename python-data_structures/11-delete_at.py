#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Si idx est négatif, return la liste sans rien faire.
    if idx < 0:
        return my_list
    # Si idx est supérieur à la range, return la liste sans rien faire.
    elif idx >= len(my_list):
        return my_list
    # Sinon, on supprime l'élément à cet indice, puis on return la liste.
    else:
        del my_list[idx]
        return my_list
