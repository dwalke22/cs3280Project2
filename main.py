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

def calculate_subnet_ipv4(ip_address, net_mask):
    """Calculates the subnet for an IPv4 address"""
    if utils.verify_ipv4(ip_address) and utils.verify_netmask(net_mask):
        if not "." in net_mask:
            mask = utils.convert_netmask(net_mask)
            subnet = utils.calculate_ipv4_subnet(ip_address, mask)
            print("Subnet for IP: %s with netmask: %s is: %s" % (ip_address, mask, subnet))
        else:
            subnet = utils.calculate_ipv4_subnet(ip_address, net_mask)
            print("Subnet for IP: %s with netmask: %s is: %s" % (ip_address, net_mask, subnet))
    else:
        print("IP Address or Net Mask is not Real")

def calculate_subnet_ipv6(ip_address, net_mask):
    """Calculates the subnet for an IPv6 address"""
    if utils.verify_ipv6(ip_address) and utils.verify_netmask(net_mask):
        print("Calculating")
    else:
        print("IP Address or Net Mask is not Real")

def main():
    """Main entry point of prgram."""
    ip_address = input("Please enter an IP Adress: ")
    net_mask = input("Please enter a subnet mask: ")
    letter_regex = re.compile(r'[a-zA-Z:]')
    if ip_address is None:
        raise ValueError('IP Adress cannot be None.')
    if net_mask is None:
        raise ValueError('Net Mask cannot be None.')
    if letter_regex.search(ip_address):
        calculate_subnet_ipv6(ip_address, net_mask)
    else:
        calculate_subnet_ipv4(ip_address, net_mask)

if __name__ == "__main__":
    main()
