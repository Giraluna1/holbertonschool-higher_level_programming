#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        except (TypeError, ValueError):
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            new.append(result)
    return new
