#!/usr/bin/env python3
"""
Script for calculating the subnet for an IP and mask

Subnet Calculation
Given an IP address (IPv4 or IPv6) and mask
a bitwise-And calculation will be performed.
"""
import re
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

def main():
    """Main entry point of prgram."""
    ip = input("Please enter an IP Adress: ")
    net_mask = input("Please enter a subnet mask: ")
    letter_regex = re.compile(r'[a-zA-Z:]')
    if letter_regex.search(ip):
        utils.verify_ipv6(ip)
    else:
        utils.verify_ipv4(ip)

    

if __name__ == "__main__":
    main()
