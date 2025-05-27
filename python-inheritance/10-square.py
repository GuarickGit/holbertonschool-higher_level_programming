#!/usr/bin/python3
"""
Ce module contient la définition d'une classe de carré,
qui hérite de la classe Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré, hérite de Rectangle et utilise une seule
    dimension pour définir la largeur et la hauteur.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square avec une taille donnée.
        La taille est validée comme un entier positif.
        """
        self.integer_validator("size", size)
        # Appelle le constructeur de Rectangle avec size pour la largeur
        # et la hauteur car un carré est un rectangle avec des côtés égaux
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule et retourne l’aire du carré.
        """
        return self.__size * self.__size
