#!/usr/bin/python3
"""
Ce module définit des classes représentant des comportements spécifiques
(nager, voler) et une classe Dragon qui combine ces comportements.
Permet de tester les capacités d’un dragon via des mixins.
"""


class SwimMixin:
    """Mixin qui ajoute la capacité de nager."""

    def swim(self):
        """Affiche un message indiquant que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin qui ajoute la capacité de voler."""

    def fly(self):
        """Affiche un message indiquant que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe représentant un dragon capable de voler, nager et rugir."""

    def roar(self):
        """Affiche un rugissement de dragon."""
        print("The dragon roars!")
