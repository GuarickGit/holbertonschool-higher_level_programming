#!/usr/bin/python3
"""Ce module fournit une fonction pour vérifier si un objet est exactement
une instance d'une classe donnée, sans prendre en compte l'héritage.
"""


def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est exactement une instance de la
    classe spécifiée.

    Cette fonction vérifie si le type de "obj" est strictement égal à
    "a_class", sans prendre en compte l'héritage.

    Arguments :
        obj : l'objet à tester.
        a_class : la classe avec laquelle comparer.

    Return :
        True si "obj" est exactement une instance de "a_class", sinon False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
