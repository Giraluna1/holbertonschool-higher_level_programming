#!/usr/bin/python3
def element_at(my_list, idx):
    range = len(my_list)
    if (idx < 0) and (idx > range):
        return (None)
    else:
        return (my_list[idx])
