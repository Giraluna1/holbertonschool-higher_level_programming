#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = ord(i)
        if (x >= 97) and (x <= 122):
            x = ord(i) - 32
        print('{:c}'.format(x), end='')
    print()
