#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    l = len(argv - 1)
    if l == 1:
        print("{:d} argument:".format(l))
    elif l == 0:
        print("0 arguments.")
    elif l > 1:
        print("{:d} arguments:".format(l))
    for i, args in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, args))
