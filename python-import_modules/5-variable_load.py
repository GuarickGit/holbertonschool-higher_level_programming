#!/usr/bin/python3

# Vérifie si le script est exécuté directement (et non importé)
if __name__ == "__main__":
    # On importe uniquement la variable 'a' depuis le module 'variable_load_5'
    from variable_load_5 import a

    # On affiche la valeur de la variable 'a'
    print("{}".format(a))
