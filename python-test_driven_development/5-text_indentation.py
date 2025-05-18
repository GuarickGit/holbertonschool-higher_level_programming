#!/usr/bin/python3
"""Module that prints text with two new lines after '.', '?' and ':'
characters."""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':' character.

    Args:
        text (str): The text to process and print.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    buffer = ""

    while i < len(text):
        char = text[i]

        if char in ".?:":
            print(buffer.strip(), end="")
            print(char, end="\n\n")
            buffer = ""

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        buffer += char
        i += 1

    if buffer.strip():
        print(buffer.strip(), end="")
    elif text.strip() == "":
        print()
