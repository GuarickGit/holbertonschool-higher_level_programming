#!/usr/bin/python3
"""Module définissant une classe Rectangle avec gestion de la largeur
   et de la hauteur."""


class Rectangle:
    """Classe représentant un rectangle avec une largeur et une hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): Largeur du rectangle (par défaut 0).
            height (int): Hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter de la largeur du rectangle.

        Returns:
            int: La largeur actuelle du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter de la largeur du rectangle.

        Args:
            value (int): Nouvelle valeur pour la largeur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter de la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter de la hauteur du rectangle.

        Args:
            value (int): Nouvelle valeur pour la hauteur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
