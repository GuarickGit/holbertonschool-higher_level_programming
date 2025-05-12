#!/usr/bin/python3

def multiple_returns(sentence):
    # Calcul de la longueur de la chaîne.
    length = len(sentence)
    # Si la string est vide, on return la length et None comme premier char.
    if sentence == "":
        return (length, None)
    # Sinon, on return la length et le premier char de la string.
    else:
        return (length, sentence[0])
