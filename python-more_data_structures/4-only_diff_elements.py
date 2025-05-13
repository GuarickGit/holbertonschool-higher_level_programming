#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # On récupère les éléments non-communs entre les deux ensembles
    uncommon = set_1.symmetric_difference(set_2)

    # On retourne l'ensemble des éléments non-communs
    return uncommon
