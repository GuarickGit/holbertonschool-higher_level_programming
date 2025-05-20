#!/usr/bin/python3
"""Module définissant une classe Rectangle avec gestion de la largeur et
   de la hauteur."""


class Rectangle:
    """Représente un rectangle défini par sa largeur et sa hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): Largeur du rectangle (valeur par défaut : 0).
            height (int): Hauteur du rectangle (valeur par défaut : 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Renvoie la largeur du rectangle.

        Returns:
            int: La largeur actuelle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur du rectangle.

        Args:
            value (int): Nouvelle valeur de la largeur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Renvoie la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur du rectangle.

        Args:
            value (int): Nouvelle valeur de la hauteur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et renvoie l'aire du rectangle.

        Returns:
            int: Aire (largeur * hauteur).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calcule et renvoie le périmètre du rectangle.

        Returns:
            int: Périmètre (2 * (largeur + hauteur)), ou 0 si l’un
            des côtés est nul.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
