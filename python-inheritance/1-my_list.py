#!/usr/bin/python3
"""Ce module définit une classe qui hérite de list et ajoute une méthode pour
afficher la liste triée."""


class MyList(list):
    """MyList est une sous-classe de list qui permet d'afficher les éléments
    triés sans modifier la liste."""

    def print_sorted(self):
        """Affiche les éléments de la liste triés par ordre croissant sans
        modifier la liste originale."""

        sorted_list = sorted(self)
        print(sorted_list)
