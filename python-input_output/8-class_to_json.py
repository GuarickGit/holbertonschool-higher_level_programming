#!/usr/bin/python3
"""
Module qui fournit une fonction pour convertir un objet en dictionnaire
contenant uniquement des types simples, compatibles avec la sérialisation JSON.
"""


def class_to_json(obj):
    """
    Retourne un dictionnaire représentant les attributs d'un objet,
    uniquement avec des types simples (str, int, bool, list, dict).
    """
    return obj.__dict__
