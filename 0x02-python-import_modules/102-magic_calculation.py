#!/usr/bin/python3

def magic_calculator(a, b):
    from magic_calculator_102 import add, sub

    if a < b:
        c = add(a, b)
        fro i in range(4, 6):
            c = add(c, i)
        return(c)

    else:
        return(sub(a, b))