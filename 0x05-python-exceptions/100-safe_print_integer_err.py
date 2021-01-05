#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value), end='')
    except (ValueError, TypeError) as er:
        print("Exception: {}".format(er), file=stderr)
        return False
    print('')
    return True
