#!/usr/bin/python3
"""Module définissant une classe Rectangle.

Cette classe permet de créer des rectangles avec une largeur et une hauteur
données, et fournit des méthodes pour calculer leur aire, leur périmètre,
ainsi qu'une représentation visuelle personnalisable à l'aide de `print_symbol`.
"""


class Rectangle:
    """Classe représentant un rectangle défini par une largeur et une hauteur.

    Attributs de classe :
        number_of_instances (int): Compte le nombre d'instances actives.
        print_symbol (any): Symbole utilisé pour la représentation visuelle
                        (converti en str lors de l'affichage).

    Méthodes publiques :
        area(): Retourne l'aire du rectangle.
        perimeter(): Retourne le périmètre du rectangle.
    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle avec largeur et hauteur optionnelles.

        Args:
            width (int): Largeur du rectangle (défaut: 0).
            height (int): Hauteur du rectangle (défaut: 0).
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Récupère la largeur actuelle du rectangle.

        Returns:
            int: La largeur du rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): Nouvelle largeur.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la largeur est négative.
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
        """Renvoie une représentation visuelle du rectangle.

        Utilise le symbole stocké dans `print_symbol` (converti en str
        si nécessaire) pour construire une chaîne composée de lignes
        correspondant à la hauteur et à la largeur du rectangle.

        Returns:
            str: Représentation textuelle, ou chaîne vide si width ou
            height est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for row in range(self.__height):
            rect_lines.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Renvoie une représentation formelle du rectangle.

        Cette chaîne permet de recréer une instance identique via eval().

        Returns:
            str: Chaîne de la forme 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Méthode appelée lors de la suppression d'une instance.

        Affiche un message de fin et décrémente le compteur
        `number_of_instances`.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
