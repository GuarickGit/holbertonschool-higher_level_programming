#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Liste qui va contenir les résultats des divisions
    new_list = []
    # Variable pour stocker temporairement le résultat d'une division
    result = 0

    # On parcourt les indices de 0 jusqu'à list_length - 1
    for i in range(list_length):
        # On tente de diviser les éléments à l'indice i des deux listes
        try:
            result = my_list_1[i] / my_list_2[i]
            # Si tout se passe bien, on ajoute le résultat à la nouvelle liste
            new_list.append(result)
        # Si l'indice dépasse la taille d'une des listes
        except IndexError:
            print("out of range")
            # On ajoute 0 à la place du résultat
            new_list.append(0)
        # Si un des éléments n'est pas un nombre (int ou float)
        except TypeError:
            print("wrong type")
            # On ajoute 0 à la place du résultat
            new_list.append(0)
        # Si on tente une division par zéro
        except ZeroDivisionError:
            print("division by 0")
            # On ajoute 0 à la place du résultat
            new_list.append(0)
        # Bloc exécuté à chaque itération, qu'une exception ait eu lieu ou non.
        finally:
            pass

# On retourne la liste des résultats
    return new_list
