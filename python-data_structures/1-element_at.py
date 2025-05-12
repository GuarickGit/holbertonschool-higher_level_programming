#!/usr/bin/python3

def element_at(my_list, idx):
        # Si idx est négatif, return None.
        if idx < 0:
            return None
        # Si idx est supérieur à la range, return None.
        elif idx > len(my_list) - 1:
            return None
        # Sinon, return l'index dans "my_list"
        else:
            return my_list[idx]
