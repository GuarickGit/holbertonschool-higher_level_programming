#!/usr/bin/python3
def fizzbuzz():
    # Boucle de 1 à 100.
    for number in range(1, 101):
        # Si modulo de 3 ET 5, alors print "FizzBuzz"
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        # Sinon si modulo de 3, alors print "Fizz".
        elif number % 3 == 0:
            print("Fizz ", end="")
        # Sinon si modulo de 5, alors print "Buzz".
        elif number % 5 == 0:
            print("Buzz ", end="")
        # Sinon, print number tel quel, avec un espace.
        else:
            print(number, end=" ")
