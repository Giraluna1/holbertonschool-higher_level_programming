#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    n = len(sys.argv)
    if n is not 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    a = int(a)
    b = int(b)
    if operator == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif operator == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif operator == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif operator == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
