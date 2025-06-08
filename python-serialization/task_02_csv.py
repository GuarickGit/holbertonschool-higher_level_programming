#!/usr/bin/python3
"""Ce module fournit une fonction pour convertir un fichier CSV
en fichier JSON en utilisant la sérialisation.
"""

import csv
import json


def convert_csv_to_json(filename):
    """Convertit un fichier CSV en fichier JSON.

    Lit les données d'un fichier CSV, les transforme en une liste
    de dictionnaires, puis les écrit dans un fichier JSON nommé data.json.

    Args:
        filename (str): Le nom du fichier CSV à lire.

    Returns:
        bool: True si la conversion a réussi, sinon False.
    """
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False
