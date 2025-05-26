#!/usr/bin/python3
"""Module qui contient la fonction is_kind_of_class."""


def is_kind_of_class(obj, a_class):
     """
    Retourne True si obj est une instance de a_class ou d'une classe héritée
    de a_class.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe de référence.

    Returns:
        True si obj est une instance ou hérite de a_class, sinon False.
    """
     if isinstance(obj, a_class):
        return True
     else:
        return False
