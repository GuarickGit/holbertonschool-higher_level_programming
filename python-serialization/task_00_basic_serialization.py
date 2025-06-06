#!/usr/bin/python3

"""
Module de sérialisation et désérialisation de dictionnaires Python au format JSON.
Permet d'enregistrer un dictionnaire dans un fichier JSON et de le recharger.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    Args:
        data (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier dans lequel sauvegarder les données JSON.
    """
    # Ouvrir le fichier en écriture (remplace le fichier s'il existe déjà)
    with open(filename, "w") as f:
        # Sérialisation et écriture dans le fichier
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Charge et désérialise un fichier JSON en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        dict: Le dictionnaire Python obtenu à partir du fichier JSON.
    """
    # Ouvrir le fichier en lecture
    with open(filename, "r") as f:
        # Lecture et désérialisation du contenu JSON
        return json.load(f)
