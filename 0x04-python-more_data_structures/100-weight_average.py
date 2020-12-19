#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = int()
    deno = int()
    for item in my_list:
        num += item[0] * item[1]
        deno += item[1]
    return float(num)/float(deno)
