#!/usr/bin/python3
"""
Module définissant une hiérarchie de classes pour des formes géométriques.

Contient une classe de base `BaseGeometry` avec des outils de validation,
et une classe `Rectangle` qui représente un rectangle avec largeur et hauteur.
"""


class BaseGeometry:
    """
    Classe de base pour représenter des formes géométriques.

    Fournit une méthode abstraite `area` et un validateur d'entiers
    pour les attributs numériques des sous-classes.
    """

    def area(self):
        """
        Méthode à implémenter dans les sous-classes pour calculer la surface.

        Lève :
            Exception: pour indiquer que cette méthode n'est pas encore
            définie.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que la valeur fournie est un entier strictement positif.

        Args:
            name (str): Nom de l'attribut (utilisé dans les messages d'erreur).
            value (int): Valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, héritée de BaseGeometry.

    Valide les dimensions fournies lors de l’instanciation.
    """

    def __init__(self, width, height):
        """
        Initialise un nouveau rectangle après validation des dimensions.

        Args:
            width (int): La largeur du rectangle (doit être > 0).
            height (int): La hauteur du rectangle (doit être > 0).

        Raises:
            TypeError, ValueError: Si les valeurs sont invalides.
        """
        # Vérifie que width et height sont des entiers strictement positifs.
        # Utilise la méthode héritée de BaseGeometry pour centraliser
        # la logique de validation.
        # Les noms "width" et "height" sont passés pour apparaître clairement
        # dans les messages d'erreur si la validation échoue.
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
