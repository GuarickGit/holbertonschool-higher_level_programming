#!/usr/bin/python3
"""
Ce module contient une fonction permettant de convertir
une chaîne JSON en objet Python.
"""

import json


def from_json_string(my_str):
    """
    Retourne un objet Python à partir de sa représentation
    sous forme de chaîne JSON.
    """
    return json.loads(my_str)
