#!/usr/bin/python3
# La première ligne indique au système d'exploitation d'utiliser l'interpréteur Python 3 pour exécuter ce script.

import importlib.util
import os
# On importe les modules nécessaires :
# - 'importlib.util' permet de charger dynamiquement des modules à partir d'un fichier.
# - 'os' n'est pas utilisé directement ici, donc on peut potentiellement le retirer, mais il peut être utile pour d'autres opérations liées au système.

def discover_names():
    # Définition de la fonction 'discover_names' qui contient toute la logique de notre script.

    # Chemin du fichier .pyc
    file_path = '/tmp/hidden_4.pyc'
    # On définit le chemin absolu du fichier compilé 'hidden_4.pyc', qui est dans le répertoire '/tmp/'.
    # Ce fichier contient du code Python compilé, et on souhaite l'importer dans notre programme.

    # Charger le module compilé
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    # On crée une "spécification" du module avec 'spec_from_file_location'.
    # Cela permet de définir un module à partir d'un fichier spécifique (ici le fichier .pyc situé à 'file_path').
    # "hidden_4" est le nom du module que l'on va charger, et il correspond au fichier .pyc.

    hidden_4 = importlib.util.module_from_spec(spec)
    # 'module_from_spec' crée un module à partir de la spécification que l'on vient de définir.
    # Cela permet de préparer le module à l'exécution, mais il n'est pas encore exécuté.

    spec.loader.exec_module(hidden_4)
    # On utilise ensuite 'exec_module' pour exécuter effectivement le module.
    # Cela charge le code contenu dans 'hidden_4.pyc' dans l'environnement d'exécution de Python.
    # Après cette ligne, les fonctions et variables définies dans 'hidden_4.pyc' sont accessibles via 'hidden_4'.

    # Récupérer les noms définis dans le module
    names = dir(hidden_4)
    # 'dir()' est une fonction Python qui renvoie la liste des attributs d'un objet (dans ce cas, un module).
    # Cela nous donne une liste de tous les noms (fonctions, variables, classes, etc.) définis dans le module 'hidden_4'.

    # Filtrer et trier les noms
    filtered_names = [name for name in names if not name.startswith("__")]
    # On crée une nouvelle liste 'filtered_names' en filtrant tous les noms qui commencent par "__".
    # Les noms qui commencent par "__" sont des noms réservés par Python (comme les méthodes spéciales '__init__').
    # Ainsi, on ignore ces noms et on ne garde que les noms d'intérêt.

    filtered_names.sort()
    # On trie les noms restants par ordre alphabétique.

    # Afficher les noms un par un
    for name in filtered_names:
        print(name)
    # On parcourt la liste 'filtered_names' et on affiche chaque nom sur une nouvelle ligne avec 'print()'.
    # Cela va afficher les noms dans l'ordre alphabétique, un par un.

if __name__ == "__main__":
    discover_names()
    # Cette ligne vérifie si le script est exécuté directement (pas importé dans un autre module).
    # Si c'est le cas, on appelle la fonction 'discover_names()' pour exécuter le programme.
    # Cela permet de garantir que le code de découverte des noms ne s'exécute pas si ce fichier est importé dans un autre programme.

    # Merci ChatMcQueen pour les commentaires ! 
