#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} arguements".format(x))
    elif x == 1:
        print("{} arguements".format(x))
    else:
        print("{} arguements".format(x))

    for i in range(x):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
