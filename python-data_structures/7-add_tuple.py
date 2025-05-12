#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # On récupère les deux premiers éléments de tuple_a
    a_values = tuple_a[:2]
    # Si tuple_a contient un seul élément, on ajoute un 0
    if len(a_values) == 1:
        a_values += (0,)
    # Si tuple_a est vide, on ajoute deux zéros
    elif len(a_values) == 0:
        a_values += (0, 0)

    # On récupère les deux premiers éléments de tuple_b
    b_values = tuple_b[:2]
    # Si tuple_b contient un seul élément, on ajoute un 0
    if len(b_values) == 1:
        b_values += (0,)
    # Si tuple_b est vide, on ajoute deux zéros
    elif len(b_values) == 0:
        b_values += (0, 0)

    # On additionne les premiers éléments (index 0)
    sum_0 = a_values[0] + b_values[0]
    # On additionne les deuxièmes éléments (index 1)
    sum_1 = a_values[1] + b_values[1]

    # On retourne le résultat dans un nouveau tuple
    new_tuple = (sum_0, sum_1)

    return new_tuple
