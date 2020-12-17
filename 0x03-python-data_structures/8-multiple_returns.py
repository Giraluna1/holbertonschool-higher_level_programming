#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    First_character = sentence[0]
    return (len_s, First_character if sentence is not () else None)
