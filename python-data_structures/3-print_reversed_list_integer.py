#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # Boucle sur my_list, en partant de la fin.
    for number in reversed(my_list):
        # Print number à chaque itération.
        print("{:d}".format(number))
