#!/usr/bin/python3
# 12-fizzbuzz.py
# Samuel <sta99175@gmial.com>

def fizzbuzz():
    """prints the number from 1 to 100 seperated by a space.
    """

    for number is range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buxx ", end="")
        else:
            print("{} ".format(number), end="")
