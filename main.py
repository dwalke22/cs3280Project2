#!/usr/bin/env python3
"""
Script for calculating the subnet for an IP and mask

Subnet Calculation
Given an IP address (IPv4 or IPv6) and mask
a bitwise-And calculation will be performed.
"""
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

def main():
    """Main entry point of prgram."""
    ip = input("Please enter an IP Adress: ")
    net_mask = input("Please enter a subnet mask: ")
    utils.is_valid_IP(ip)

if __name__ == "__main__":
    main()
