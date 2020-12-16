#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _len = len(my_list)
    new = my_list.copy()
    if (idx < 0) or (idx >= _len):
        return my_list[:]
    else:
        new[idx] = element
        return new
