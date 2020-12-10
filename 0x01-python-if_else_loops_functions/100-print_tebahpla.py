#!/usr/bin/python3
altern = ''
for i in reversed(range(97, 123)):
    if (i != 113) and (i != 101):
        if not i % 2:
            altern = chr(i).lower()
        else:
            altern = chr(i).upper()
        print('{}'.format(altern), end="")
