#!/usr/bin/python3
"""
Ce module illustre l'utilisation de l'héritage multiple en Python à travers
la création d'une classe FlyingFish, qui hérite de deux classes : Fish et Bird.
"""


class Fish:
    """
    Classe représentant un poisson.

    Cette classe définit les comportements génériques d'un poisson,
    notamment sa manière de nager et son habitat naturel.
    """

    def swim(self):
        """
        Affiche un message indiquant que le poisson nage.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Affiche un message décrivant l'habitat naturel du poisson.
        """
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.

    Cette classe définit les comportements génériques d'un oiseau,
    tels que voler et son habitat dans le ciel.
    """

    def fly(self):
        """
        Affiche un message indiquant que l'oiseau vole.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Affiche un message décrivant l'habitat naturel de l'oiseau.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant.

    Cette classe hérite à la fois de Fish et de Bird, et redéfinit
    certains comportements pour représenter les caractéristiques d'un
    poisson volant.
    """

    def fly(self):
        """
        Affiche un message spécifique au vol du poisson volant.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Affiche un message spécifique à la nage du poisson volant.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Affiche un message décrivant le double habitat du poisson volant.
        """
        print("The flying fish lives both in water and the sky!")
