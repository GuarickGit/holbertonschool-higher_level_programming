#!/usr/bin/python3
"""
Ce module contient une fonction permettant d’ajouter du texte
à la fin d’un fichier texte (encodé en UTF-8), et de retourner
le nombre de caractères ajoutés.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d’un fichier texte (UTF8)
    et retourne le nombre de caractères ajoutés.

    Si le fichier n'existe pas, il est créé.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
