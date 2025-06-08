#!/usr/bin/python3
"""Ce module permet de sérialiser un dictionnaire en XML
et de le désérialiser à partir d’un fichier XML.
"""

import xml.etree.ElementTree as ET  # Module standard pour manipuler du XML


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire Python dans un fichier XML.

    Args:
        dictionary (dict): Le dictionnaire à convertir.
        filename (str): Le nom du fichier XML de destination.
    """

    # Crée l'élément racine <data>
    root = ET.Element("data")

    # Pour chaque paire clé-valeur du dictionnaire:
    for key, value in dictionary.items():
        # Crée un sous-élément <clé>valeur</clé>
        child = ET.SubElement(root, key)
        # Le contenu texte de l’élément est la valeur (en string)
        child.text = str(value)

    # Crée un arbre XML complet à partir de la racine
    tree = ET.ElementTree(root)
    # Écrit l’arbre dans le fichier XML spécifié
    tree.write(filename)


def deserialize_from_xml(filename):
    """Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Le dictionnaire contenant les données extraites du fichier.
    """

    # Charge le fichier XML et crée un arbre d’éléments
    tree = ET.parse(filename)

    # Récupère l'élément racine <data>
    root = tree.getroot()

    # Dictionnaire où on va stocker les paires clé-valeur
    result = {}

    # Parcourt tous les éléments enfants de la racine
    for child in root:
        # La clé est le nom de la balise, la valeur est son contenu texte
        result[child.tag] = child.text

    # Retourne le dictionnaire reconstruit
    return result
