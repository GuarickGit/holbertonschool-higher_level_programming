#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # On récupère toutes les clés du dictionnaire sous forme de liste
    my_keys = list(a_dictionary.keys())

    # On trie la liste des clés dans l'ordre alphabétique
    my_keys.sort()

    # Pour chaque clé triée, on affiche la paire clé: valeur
    for i in my_keys:
        print(f"{i}: {a_dictionary[i]}")
