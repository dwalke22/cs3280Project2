#!/usr/bin/env python3
"""
Unit test for utils.py
"""

import unittest
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

class TestUtils(unittest.TestCase):
    def test_nonvalid_ipv6(self):
        self.assertFalse(utils.verify_ipv6("12"))

    def test_valid_ipv6_stand(self):
        self.assertTrue(utils.verify_ipv6("1762:0:0:0:0:B03:1:AF18"))

    def test_valid_ipv6_mixed(self):
        self.assertTrue(utils.verify_ipv6("1762:0:0:0:0:B03:127.32.67.15"))

    def test_nonvalid_ipv4(self):
        self.assertFalse(utils.verify_ipv4("12"))

    def test_valid_ipv4(self):
        self.assertTrue(utils.verify_ipv4("192.168.244.3"))

    def test_valid_net_number(self):
        self.assertTrue(utils.verify_netmask("20"))

    def test_valid_net_ipv4(self):
        self.assertTrue(utils.verify_netmask("160.010.25.007"))

    def test_proper_netmask_convers(self):
        expected = "11111111.11111111.00000000.00000000"
        result = utils.convert_netmask("16")
        self.assertEqual(expected, result)

    def test_proper_ipv4_net_conver(self):
        expected = "11111111.11111111.00000000.00000000"
        result = utils.convert_ip_netmask("255.255.0.0")
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
