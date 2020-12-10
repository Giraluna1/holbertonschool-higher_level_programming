#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import sys
    num_arguments = len(argv)
    argument = 1

    if num_arguments == 1:
        print('{} arguments.'.format(num_arguments-1))
    elif num_arguments == 2:
        print('{} argument:'.format(num_arguments-1))
    else:
        print('{} arguments:'.format(num_arguments-1))

    i = 1

    for argument in range(1, len(sys.argv)):
        print('{:d}: {}'.format(i, sys.argv[argument]))
        i += 1
