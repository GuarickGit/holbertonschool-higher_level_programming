#!/usr/bin/python3

def uniq_add(my_list=[]):
    # On convertit la liste en set pour supprimer les doublons
    my_set = set(my_list)

    # On calcule la somme des éléments uniques
    result = sum(my_set)

    # On retourne le résultat
    return result
