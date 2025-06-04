#!/usr/bin/python3
"""
Ce module fournit une fonction permettant d’obtenir
la représentation JSON d’un objet Python sous forme de chaîne.
"""

import json


def to_json_string(my_obj):
    """
    Retourne la représentation JSON sous forme de chaîne
    d’un objet Python donné.

    L’objet doit être sérialisable en JSON.
    """
    return json.dumps(my_obj)
