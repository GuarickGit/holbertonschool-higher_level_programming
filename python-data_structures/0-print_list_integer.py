#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # Boucle sur la length de "my_list" (Index 0 à len -1).
    for number in range(len(my_list)):
        # print chaque index de my_list.
        print("{}".format(my_list[number]))
