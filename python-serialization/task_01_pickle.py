#!/usr/bin/python3
"""Ce module définit la classe CustomObject et fournit des
méthodes pour sérialiser et désérialiser ses instances avec pickle.
"""

import pickle


class CustomObject:
    """Objet personnalisé contenant des informations personnelles
    et des méthodes de sérialisation/désérialisation.
    """

    def __init__(self, name, age, is_student):
        """Initialise une instance de CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'instance de CustomObject."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'instance actuelle dans un fichier à l'aide de pickle.

        Args:
            filename (str): Le nom du fichier dans lequel enregistrer l'objet.

        Returns:
            None si une erreur se produit lors de la sérialisation.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Désérialise une instance de CustomObject depuis un fichier.

        Args:
            filename (str): Le nom du fichier à partir duquel charger l'objet.

        Returns:
            CustomObject: L'objet désérialisé, ou None si une erreur se produit
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
