#!/usr/bin/python3
"""Module définissant la classe Square.

Ce module fournit une implémentation de base d'un carré avec un attribut privé
pour représenter sa taille. Cette version ne comporte aucune vérification de
type ou de valeur pour l'attribut de taille.
"""


class Square:
    """Classe représentant un carré.

    Cette classe définit un carré avec une taille, stockée comme attribut
    privé. Aucun contrôle de type ou de valeur n’est effectué à ce stade.
    """

    def __init__(self, size):
        """Initialise une nouvelle instance de la classe Square.

        Args:
            size: La taille du carré (pas de vérification de type/valeur ici).
        """
        self.__size = size
