#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if type(roman_string) is not str or roman_string is None:
        return (0)
    for i, char in enumerate(roman_string):
        tmp = roman[char]
        try:
            if tmp < roman[roman_string[i + 1]]:
                tmp = tmp * -1
        except IndexError:
            pass
        number = number + tmp
    return number
