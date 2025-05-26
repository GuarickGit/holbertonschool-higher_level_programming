#!/usr/bin/python3
"""
Module qui définit la fonction inherits_from.

Ce module contient une fonction permettant de vérifier si un objet
est une instance d'une classe qui hérite (directement ou indirectement)
d'une classe spécifiée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet est une instance d'une sous-classe de a_class.

    Args:
        obj: L'objet à tester.
        a_class: La classe de référence.

    Returns:
        True si obj est une instance d'une classe qui hérite de a_class
        (mais n'est pas directement une instance de a_class),
        False sinon.
    """
    # On vérifie que la classe de obj hérite de a_class
    # et qu'elle n'est pas exactement a_class elle-même
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
