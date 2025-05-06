#!/usr/bin/python3

# Boucle de 0 à 99
for numbers in range(0, 100):
    if numbers < 99:
        # Print de 0 à 98, avec 2 digits, et un espace.
        print("{0:0=2d},".format(numbers), end=" ")
    else:
        # Print 99, avec 2 digits, sans virgule et sans espace.
        print("{0:0=2d}".format(numbers))
