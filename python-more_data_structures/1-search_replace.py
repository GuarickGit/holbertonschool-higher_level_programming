#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Création d'une nouvelle liste vide pour stocker le résultat
    new_list = []

    # Parcours de chaque élément dans la liste d'origine
    for number in my_list:
        # Si l'élément est égal à celui qu'on cherche à remplacer
        if number == search:
            # On ajoute l'élément de remplacement à la nouvelle liste
            new_list.append(replace)
        else:
            # Sinon, on ajoute l'élément tel quel
            new_list.append(number)
    # On retourne la nouvelle liste avec les remplacements effectués
    return new_list
