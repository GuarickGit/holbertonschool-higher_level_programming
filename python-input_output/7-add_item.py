#!/usr/bin/python3
"""
Ce script ajoute tous les arguments passés en ligne de commande
dans une liste Python, puis les sauvegarde dans un fichier JSON.
Le fichier utilisé est 'add_item.json'. Il est créé s’il n’existe pas.
"""

import sys  # Pour récupérer les arguments passés au script
import os  # Pour vérifier si le fichier existe
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Si le fichier existe, on charge la liste à partir de celui-ci
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    # Sinon, on part d'une liste vide
    my_list = []

# On ajoute les arguments passés au script (en ignorant le nom du script)
my_list.extend(sys.argv[1:])

# On sauvegarde la nouvelle liste dans le fichier JSON
save_to_json_file(my_list, "add_item.json")
