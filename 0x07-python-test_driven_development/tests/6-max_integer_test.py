#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    "hello"
    def test(self):
        "hello"
        v1 = [76]
        self.assertEqual(max_integer(v1), 76)
