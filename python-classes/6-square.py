#!/usr/bin/python3
"""Module définissant la classe Square.

Ce module fournit une implémentation d'un carré avec deux attributs privés :
la taille (`size`) et la position (`position`). La taille est validée pour
s'assurer qu'elle est un entier supérieur ou égal à 0. La position permet
de décaler l'affichage du carré. La classe fournit des méthodes pour calculer
l'aire du carré et l'afficher avec des caractères #.
"""


class Square:
    """Classe représentant un carré géométrique.

    Cette classe encapsule un carré avec deux attributs privés :
    la taille (`__size`) et la position (`__position`). Elle garantit que la
    taille est toujours un entier positif ou nul, et que la position est un
    tuple de deux entiers positifs. Elle permet de calculer l'aire du carré
    ou de l'afficher à l'écran avec un décalage.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise une nouvelle instance de la classe Square.

        Args:
        size (int, optional): La taille du carré (longueur d’un côté).
            Doit être un entier supérieur ou égal à 0. Par défaut 0.
        position (tuple, optional): Un tuple de 2 entiers positifs représentant
            le décalage horizontal et vertical lors de l’affichage. Par défaut (0, 0).

        Raises:
            TypeError: Si size n'est pas un entier ou si position est invalide.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if (not isinstance(position, tuple)) or len(position) != 2 or not all(
                isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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
        Sinon, affiche un carré de taille `size` x `size` composé de `#`,
        avec un décalage horizontal (`position[0]`) et vertical (`position[1]`)
        défini par l’attribut position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)) or len(value) != 2 or not all(
                isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
