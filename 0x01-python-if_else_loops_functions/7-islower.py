#!/usr/bin/python3
# 7-islower.py
# samuel stanley <sta99175@gmail.com>

def islower(c):
    """checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
