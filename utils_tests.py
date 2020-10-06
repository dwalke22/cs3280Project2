#!/usr/bin/env python3
"""
Unit test for utils.py
"""

import unittest
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

class TestUtils(unittest.TestCase):
    def test_none_ipv6(self):
        self.assertRaises(ValueError, utils.verify_ipv6, None)

    def test_nonvalid_ipv6(self):
        self.assertFalse(utils.verify_ipv6("12"))

    def test_valid_ipv6_stand(self):
        self.assertTrue(utils.verify_ipv6("1762:0:0:0:0:B03:1:AF18"))

    def test_valid_ipv6_mixed(self):
        self.assertTrue(utils.verify_ipv6("1762:0:0:0:0:B03:127.32.67.15"))

    def test_none_ipv4(self):
        self.assertRaises(ValueError, utils.verify_ipv4, None)

    def test_nonvalid_ipv4(self):
        self.assertFalse(utils.verify_ipv4("12"))

    def test_valid_ipv4(self):
        self.assertTrue(utils.verify_ipv4("192.168.244.3"))

if __name__ == "__main__":
    unittest.main()
