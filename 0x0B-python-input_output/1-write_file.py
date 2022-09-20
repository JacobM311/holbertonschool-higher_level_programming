#!/usr/bin/python3
"""
writes and returns the number of characters
"""


def write_file(filename="", text=""):
    """returns the number of lines of a text file"""
    with open(filename, mode="w", encoding='utf8') as f:
        return(f.write(text))
