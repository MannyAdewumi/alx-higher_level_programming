#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    if a_dictionary:
        for key, value in a_dictionary.item():
            new_dic.update({key: value * 2})
        return new_dic
