#!/usr/bin/python3
"""Module définissant un itérateur comptant le nombre d’éléments parcourus."""


class CountedIterator:
    """Classe personnalisée qui permet d’itérer sur un objet tout en comptant
    les éléments parcourus."""

    def __init__(self, iterable):
        """
        Initialise l'objet avec un itérable.

        L'objet crée un itérateur interne et initialise un compteur à zéro.
        """
        # Crée un itérateur à partir de l’itérable fourni
        self.iterable = iter(iterable)
        # Initialise le compteur à zéro
        self.count = 0

    def __next__(self):
        """
        Renvoie l’élément suivant de l’itérateur et incrémente le compteur.

        Lève StopIteration quand il n’y a plus d’éléments.
        """
        value = next(self.iterable)  # Récupère l’élément suivant
        self.count += 1  # Incrémente le compteur
        return value  # Renvoie l’élément

    def get_count(self):
        """
        Renvoie le nombre d’éléments déjà parcourus.
        """
        return self.count  # Retourne le compteur

    def __iter__(self):
        """
        Renvoie l’objet lui-même en tant qu’itérateur.

        Permet d’utiliser l’objet dans une boucle.
        """
        return self  # Retourne l’objet pour les boucles
