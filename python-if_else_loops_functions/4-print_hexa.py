#!/usr/bin/python3

# Boucle de 0 à 98
for number in range(0, 99):
    # Print Number en Décimal, "=", puis 0x"HEX" (équivalence HEXA en ASCII)
    print("{} = ".format(number) + hex(number))
