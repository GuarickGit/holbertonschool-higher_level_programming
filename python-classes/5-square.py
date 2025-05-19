#!/usr/bin/python3
"""Module définissant la classe Square.

Ce module fournit une implémentation d'un carré avec une taille privée.
La taille est validée pour s'assurer qu'elle est un entier supérieur ou
égal à 0. La classe fournit des méthodes pour calculer l'aire du carré
et l'afficher avec des caractères #.
"""


class Square:
    """Classe représentant un carré géométrique.

    Cette classe encapsule un carré avec un attribut de taille privé.
    Elle garantit que la taille est toujours un entier positif ou nul,
    et permet de calculer l'aire du carré ou de l'afficher en console.
    """

    def __init__(self, size=0):
        """Initialise une nouvelle instance de la classe Square.

        Args:
            size (int, optional): La taille du carré (longueur d’un côté).
            Doit être un entier supérieur ou égal à 0. La valeur par défaut
            est 0.

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
            int: L'aire du carré, calculée comme size ** 2.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Récupère la taille actuelle du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré avec validation.

        Args:
            value (int): La nouvelle taille à affecter au carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Affiche une représentation visuelle du carré avec le caractère #.

        Si la taille du carré est 0, affiche simplement une ligne vide.
        Sinon, affiche un carré de taille `size` x `size` composé de `#`.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.size)
