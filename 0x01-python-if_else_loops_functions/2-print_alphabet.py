#!/usr/bin/python3
# 2-print_alphabet.py
# samuel stanley <sta99175@gmail.com>

"""Prints alphabet in lower, not followed by a new line. """
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
