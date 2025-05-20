#!/usr/bin/python3
"""Module définissant une classe Rectangle.

Cette classe permet de créer des rectangles avec une largeur et une hauteur
données, et fournit des méthodes pour calculer leur aire, périmètre, ainsi
qu'une représentation textuelle avec le caractère `#`.
"""


class Rectangle:
    """Classe représentant un rectangle avec largeur et hauteur.

    Attributs de classe:
        number_of_instances (int): Compte le nombre d'instances
        actives de Rectangle.

    Fournit des méthodes pour calculer l'aire, le périmètre,
    et afficher une représentation visuelle ou formelle du rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): Largeur du rectangle (par défaut 0).
            height (int): Hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Renvoie une représentation visuelle du rectangle avec
        le caractère `#`.

        Retourne une chaîne composée de lignes de `#`, dont le nombre
        correspond à la hauteur et la largeur du rectangle.

        Returns:
            str: Représentation textuelle ou chaîne vide si l'une des
            dimensions est nulle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for row in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Renvoie une chaîne de caractères représentant le rectangle de façon
        non ambiguë, pouvant être utilisée avec eval() pour recréer une
        instance identique.

        Returns:
            str: Représentation formelle du rectangle sous la forme
             'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message lors de la suppression de l'instance.

        Cette méthode spéciale est appelée automatiquement lorsque
        l'objet Rectangle est détruit (par exemple via del ou en
        fin de programme).
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
