#!/usr/bin/python3
for num_one in range(0, 10):
    for num_two in range(num_one + 1, 10):
        if num_one == 8 and num_two == 9:
            print("{}{}".format(num_one, num_two))
        else:
            print("{}{}, ".format(num_one, num_two), end='')
