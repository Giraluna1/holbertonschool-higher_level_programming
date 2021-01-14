#!/usr/bin/python3
"""
This is he module Text indetation

"""


def text_indentation(text):
    """
    print a text with 2 new lines after each of these characters

    """
    identation_text = ""
    if type(text) is not str:
        raise TypeError('text must be a string')
    else:
        replace_dot1 = text.replace('. ', '.')
        replace_dot2 = replace_dot1.replace('.', '.\n\n')
        replace_sigQ1 = replace_dot2.replace('? ', '?')
        replace_sigQ2 = replace_sigQ1.replace('?', '?\n\n')
        replace_2dot1 = replace_sigQ2.replace(': ', ':')
        replace_2dot2 = replace_2dot1.replace(':', ':\n\n')
        print(replace_2dot2, end='')
