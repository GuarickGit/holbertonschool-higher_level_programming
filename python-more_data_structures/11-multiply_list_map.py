#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # Utilise map pour appliquer une multipli. à chaque élément de la liste
    # Lambda prend chaque élément x de my_list et retourne x * number
    # map retourne un itérable, qu'on transforme en liste avec list()
    return list(map(lambda x: x * number, my_list))
