#!/usr/bin/python3
"""
appends file and return number of characters
"""


def read_lines(filename="", text=""):
    """reads file and appends"""
    with open(filename, mode="a", encoding='utf-8') as f:
        return(f.write(text))
