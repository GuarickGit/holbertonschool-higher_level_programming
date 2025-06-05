#!/usr/bin/python3
"""
Module définissant la classe Student avec une méthode
permettant de sérialiser ses attributs en dictionnaire,
avec un filtrage optionnel.
"""


class Student:
    """
    Représente un étudiant avec un prénom, un nom et un âge.
    Fournit une méthode pour obtenir une représentation
    sérialisable en JSON.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant avec un prénom, un nom et un âge.

        Args:
            first_name (str): Prénom de l'étudiant.
            last_name (str): Nom de famille de l'étudiant.
            age (int): Âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire contenant les attributs de l'étudiant.

        Si 'attrs' est une liste de chaînes, seuls les attributs dont les noms
        sont présents dans cette liste sont inclus.

        Sinon, tous les attributs de l'instance sont retournés.

        Args:
            attrs (list, optional): Liste de noms d'attributs à inclure.
                                    Doit être une liste de chaînes.

        Returns:
            dict: Dictionnaire des attributs sélectionnés.
        """

        # Si attrs n'est pas une liste, retourner tous les attributs
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            # Sinon, créer un dictionnaire
            filtered = {}
            for attribut in attrs:
                # Vérifier si l'attribut existe dans l'objet
                if attribut in self.__dict__:
                    # Ajouter l'attribut et valeur dans le dictionnaire filtré
                    filtered[attribut] = self.__dict__[attribut]
            # Retourner le dictionnaire filtré
            return filtered
