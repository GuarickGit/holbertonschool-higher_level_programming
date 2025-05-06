#!/usr/bin/python3

# Boucle sur les dizaines (de 0 à 9)
for tens in range(0, 10):
    # Boucle sur les unités, start de tens + 1 pour éviter les doublons,
    # donc il y aura forcement tens < units.
    for units in range(tens + 1, 10):
        # Si 89, on imprime sans virgule et avec retour à la ligne.
        if tens == 8 and units == 9:
            print("{}{}".format(tens, units))
        else:
            # Sinon, on imprime tens et units, une virgule,
            # et avec (end=" ") on a un espace entre chaque, et pas de \n.
            print("{}{},".format(tens, units), end=" ")
