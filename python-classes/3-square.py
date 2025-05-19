#!/usr/bin/python3
"""Module définissant la classe Square.

Ce module fournit une implémentation d'un carré avec une taille privée.
La taille est validée pour s'assurer qu'elle est un entier supérieur ou égal à 0.
La classe permet aussi de calculer l'aire du carré.
"""


class Square:
    """Classe représentant un carré.

    La classe encapsule la notion de carré avec une taille privée.
    Elle garantit que la taille est toujours un entier positif ou nul.
    """

    def __init__(self, size=0):
        """Initialise une nouvelle instance de la classe Square.

        Args:
            size (int): La taille du carré. Doit être un entier >= 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size ** 2).
        """
        return self.__size * self.__size
