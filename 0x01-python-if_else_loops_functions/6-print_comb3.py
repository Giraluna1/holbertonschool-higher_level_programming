#!/usr/bin/python3
for i in range(9):
    x = i+1
    for j in range(x, 10):
        if(i == 8) and (j == 9):
            print('{}{}'.format(i, j), end=' ')
        else:
            print('{}{}'.format(i, j), end=', ')
