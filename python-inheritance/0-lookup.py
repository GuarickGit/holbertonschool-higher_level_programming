#!/usr/bin/python3
"""Ce module fournit une fonction permettant d’obtenir les attributs et
méthodes d’un objet."""


def lookup(obj):
    """Renvoie la liste des attributs et méthodes disponibles pour un
    objet donné."""
    return dir(obj)
