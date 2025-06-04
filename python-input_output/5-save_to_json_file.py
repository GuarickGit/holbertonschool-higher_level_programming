#!/usr/bin/python3
"""
Ce module permet de sauvegarder un objet Python
dans un fichier texte au format JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet Python dans un fichier texte, en utilisant
    sa représentation JSON.

    Le fichier est écrasé s’il existe déjà.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
