#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_hidden = dir(hidden_4)
    list_hidden.sort()

    for i in list_hidden:
        if i[0] is not '_':
            print(i)
