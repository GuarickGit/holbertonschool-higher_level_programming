#!/usr/bin/python3
"""Ce module permet de lire un fichier texte en UTF-8 et d'en afficher le
contenu sur la sortie standard."""

def read_file(filename=""):
    """Lit un fichier texte UTF-8 et affiche son contenu sur la sortie
    standard."""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

