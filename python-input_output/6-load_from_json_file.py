#!/usr/bin/python3
"""
Ce module permet de charger un objet Python
à partir d’un fichier contenant une chaîne JSON.
"""

import json


def load_from_json_file(filename):
    """
    Lit un fichier contenant une chaîne JSON et retourne
    l’objet Python correspondant.
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj = f.read()
        return json.loads(obj)
