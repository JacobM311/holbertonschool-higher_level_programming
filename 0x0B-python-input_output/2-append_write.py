#!/usr/bin/python3
"""
Contains the "read_lines" function
"""


def read_lines(filename="", text=""):
    """reads file and appends"""
    with open(filename, 'r', encoding='utf-8') as f:
        return(f.write(text))
