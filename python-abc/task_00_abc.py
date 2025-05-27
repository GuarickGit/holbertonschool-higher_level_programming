#!/usr/bin/python3
"""
Module représentant des animaux avec une interface abstraite.

Ce module définit une classe abstraite `Animal` avec une méthode `sound`
à implémenter.
Les classes `Dog` et `Cat` héritent de cette interface et fournissent leur
propre implémentation de la méthode `sound`.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.

    Cette classe définit une interface commune pour tous les types d'animaux.
    Toute classe héritée doit implémenter la méthode `sound`.
    """
    @abstractmethod
    def sound(self):
        """
        Renvoie le son que fait l'animal.

        Cette méthode doit être implémentée par toutes les sous-classes.
        """
        pass


class Dog(Animal):
    """Classe représentant un chien, héritée de la classe Animal."""

    def sound(self):
        """Renvoie le son que fait un chien."""
        return "Bark"


class Cat(Animal):
    """Classe représentant un chat, héritée de la classe Animal."""

    def sound(self):
        """Renvoie le son que fait un chat."""
        return "Meow"
