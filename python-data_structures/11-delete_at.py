#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    # Si idx est négatif, return la liste sans rien faire.
    if idx < 0:
        return my_list
    # Si idx est supérieur à la range, return la liste sans rien faire.
    elif idx >= len(my_list):
        return my_list
    # Sinon, on construit une nouvelle liste sans l'élément à cet indice.
    else:
        # On construit une nouvelle liste en excluant l'élément à l'indice idx :
        # my_list[:idx] prend tous les éléments avant idx (non inclus)
        # my_list[idx + 1:] prend tous les éléments après idx (donc on saute idx)
        # On les concatène pour obtenir une nouvelle liste sans l'élément ciblé
        new_list = my_list[:idx] + my_list[idx + 1:]
        return new_list
