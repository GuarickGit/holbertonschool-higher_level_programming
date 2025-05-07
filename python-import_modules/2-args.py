#!/usr/bin/python3

#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n_arguments = len(argv) - 1

    if n_arguments == 0:
        print("0 arguments.")

    elif n_arguments == 1:
        print("1 argument:")

    elif n_arguments > 1:
        print("{} arguments:".format(n_arguments))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

