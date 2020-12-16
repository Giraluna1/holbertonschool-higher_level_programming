#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        _len = len(i)
        for j in range(0, _len):
            print('{:d}'.format(i[j]), end='')
            if j != _len - 1:
                print('', end=' ')
        print()