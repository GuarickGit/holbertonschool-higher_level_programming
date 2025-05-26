#!/usr/bin/python3
"""
Ce module contient la définition d'une classe de base pour des formes
géométriques.
"""


class BaseGeometry:
    """
    Classe de base pour représenter des formes géométriques.

    Cette classe est destinée à être étendue par des sous-classes qui
    implémenteront des fonctionnalités spécifiques comme le calcul de
    surface ou de périmètre.
    """

    def area(self):
        """
        Méthode qui devrait être implémentée dans les sous-classes pour
        calculer la surface de la forme géométrique.

        Lève :
            Exception : indique que la méthode n'est pas encore implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
