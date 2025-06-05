#!/usr/bin/python3
"""
Module définissant la classe Student avec une méthode
permettant de sérialiser ses attributs en dictionnaire.
"""


class Student:
    """
    Représente un étudiant avec un prénom, un nom et un âge.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant avec un prénom, un nom et un âge.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne un dictionnaire contenant les attributs de l'étudiant.
        Utile pour la sérialisation en JSON.
        """
        return self.__dict__
