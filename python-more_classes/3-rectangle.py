#!/usr/bin/python3
"""Module définissant une classe Rectangle.

Cette classe permet de créer des rectangles avec une largeur et une hauteur
données, et fournit des méthodes pour calculer leur aire, périmètre, ainsi
qu'une représentation textuelle avec le caractère `#`.
"""


class Rectangle:
    """Classe représentant un rectangle."""

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
        """Récupère la largeur du rectangle.

        Returns:
            int: La largeur actuelle du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): Nouvelle largeur du rectangle.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.

        Args:
            value (int): Nouvelle hauteur du rectangle.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule l'aire du rectangle.

        Returns:
            int: L'aire (largeur * hauteur).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre (2 * (largeur + hauteur)), ou 0 si l’un
                 des côtés est nul.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Renvoie une représentation en chaîne de caractères du rectangle.

        La forme est composée du caractère `#`, avec autant de lignes
        que la hauteur, et autant de `#` par ligne que la largeur.

        Returns:
            str: Représentation textuelle du rectangle, ou une chaîne vide
                 si la largeur ou la hauteur est égale à 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for row in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)
