#!/usr/bin/python3
"""
Contains the number_of_lines function
"""


def write_file(filename="", text=""):
    """returns the number of lines of a text file"""
    with open(filename, 'r', encoding='utf8') as f:
        return(f.write(text))
    i = 0
        for i, line in enumerate(f):
            print(line, end='')
