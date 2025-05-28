#!/usr/bin/python3
"""
Ce module définit la classe VerboseList qui étend la classe list.
Elle affiche un message à chaque ajout ou suppression d'élément dans la liste.
"""


class VerboseList(list):
    """
    Classe personnalisée dérivée de list, qui affiche des messages lors
    des modifications.
    """

    def append(self, object):
        """
        Ajoute un élément à la fin de la liste et affiche un message.
        """
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        """
        Ajoute plusieurs éléments à la liste depuis un itérable et
        affiche un message.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        """
        Supprime la première occurrence de la valeur spécifiée et affiche
        un message.
        """
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        """
        Supprime et retourne l’élément à l’index donné (le dernier par défaut)
        et affiche un message.
        """
        item_remove = super().pop(index)
        print(f"Popped [{item_remove}] from the list.")
