#!/usr/bin/python3
def print_last_digit(number):
    # On récupère le dernier chiffre du nombre, toujours positif.
    # abs() permet de gérer les nombres négatifs en les rendant positifs.
    last_digit = abs(number) % 10
    # Affiche le chiffre sans retour à la ligne. (end="").
    print("{}".format(last_digit), end="")
    # Retourne la valeur du dernier chiffre.
    return last_digit
