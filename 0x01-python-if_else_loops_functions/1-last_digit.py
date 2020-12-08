#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
str1 = 'Last digit of'
if number < 0:
    last = number % -10
    print(end='')
if last > 5:
    print(str1 + ' {} is {} and is greater than 5'.format(number, last))
elif last == 0:
    print(str1 + ' {} is {} and is 0'.format(number, last))
else:
    print(str1 + ' {} is {} and is less than 6 and not 0'.format(number, last))
