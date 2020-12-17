#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    First_character = (sentence[0] if sentence else None)
    return (len_s, First_character)
