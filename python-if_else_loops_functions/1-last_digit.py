#!/usr/bin/python3
# Importe le moule 'random'
import random
# number contient un chiffre aléatoire entre -10000 et 10000 à chaque run.
number = random.randint(-10000, 10000)
# last_digit contient les deux last digit absolu (abs) de number.
last_digit = abs(number) % 10

# Si number inférieur à zéro, alors last_digit devient -last_digit (négatif)
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
