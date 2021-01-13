#!/usr/bin/python3
def magic_string(_list=[]):
    _list.append("Holberton")
    return ', '.join(_list)

for i in range(10):
    print(magic_string())