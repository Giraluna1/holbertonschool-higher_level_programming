#!/usr/bin/python3
def uniq_add(my_list=[]):
    # obtenemos los elementos de la lista sin repetir
    uniq_idx = list(set(my_list))
    # sumamos esos unicos elementos
    result = sum(uniq_idx)
    return result
