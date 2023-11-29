#!/usr/bin/python3
# 6-print_combs.py
# samuel <sta99175@gmail.com>

"""This will print all possible different combination of two digits in ascending order.
both digits must be different - 01 and 10 are considered identical"""

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and difit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")

