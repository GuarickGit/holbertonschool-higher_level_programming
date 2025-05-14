#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Supprime la clé du dictionnaire si elle existe.
    # Si la clé n'existe pas, ne fait rien
    # (grâce à la valeur par défaut dans .pop()).
    a_dictionary.pop(key, "missing key")
    # Retourne le dictionnaire mis à jour
    return a_dictionary
