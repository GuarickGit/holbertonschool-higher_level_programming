#!/usr/bin/python3

def max_integer(my_list=[]):
    # Si la liste est vide, on retourne None
    if my_list == []:
        return None

    # On initialise la variable max_value avec le premier élément de la liste
    max_value = my_list[0]

    # On parcourt le reste de la liste à partir du deuxième élément
    for i in my_list[1:]:
        # Si on trouve un élément plus grand que max_value, on le remplace
        if i > max_value:
            max_value = i

    # Une fois la boucle terminée, on retourne la plus grande valeur trouvée
    return max_value
