#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        n = number * -1
        last = n % 10
        print('{:d}'.format(last), end='')
    else:
        last = number % 10
        print('{:d}'.format(last), end='')
    return last
