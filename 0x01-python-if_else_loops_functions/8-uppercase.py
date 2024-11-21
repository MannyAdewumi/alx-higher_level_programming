#!/usr/bin/python3
def uppercase(str):
    for iterate in str:
        temp = iterate
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(iterate) - 32)
        print("{}".format(temp), end='')
    print()
