#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    "hello"
    def test_one_element(self):
        """Tests for only one number in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)
