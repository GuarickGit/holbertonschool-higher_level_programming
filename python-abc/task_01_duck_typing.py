#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique."""
    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme."""
        pass


class Circle(Shape):
    """Classe représentant un cercle avec un rayon donné."""

    def __init__(self, radius):
        """Initialise un cercle avec le rayon fourni."""
        super().__init__()
        self.radius = radius

    def area(self):
        """Retourne l'aire du cercle."""
        return self.radius * self.radius * math.pi

    def perimeter(self):
        """Retourne le périmètre (circonférence) du cercle."""
        return (self.radius * 2) * math.pi


class Rectangle(Shape):
    """Classe représentant un rectangle avec une largeur et une hauteur."""

    def __init__(self, width, height):
        """Initialise un rectangle avec la largeur et la hauteur fournies."""
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        return (self.width + self.height) * 2


def shape_info(obj):
    """Affiche l'aire et le périmètre d'une forme donnée,
    sans vérifier son type."""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
