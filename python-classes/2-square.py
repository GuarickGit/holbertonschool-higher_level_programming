#!/usr/bin/python3
"""Module définissant la classe Square.

Ce module fournit une implémentation de base d'un carré avec un attribut privé
pour représenter sa taille. La taille est validée pour s'assurer qu'elle est
un entier supérieur ou égal à 0.
"""


class Square:
    """Classe représentant un carré.

    Cette classe définit un carré avec une taille, stockée comme attribut
    privé. La taille doit être un entier supérieur ou égal à 0.
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

