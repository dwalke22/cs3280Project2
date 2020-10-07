#!/usr/bin/env python3
"""
Provides utility method for bitwises-Add
"""
import re

def verify_ipv6(ip_address):
    """Verifies that the ip is a valid IPv6 address"""
    ip_regex = re.compile(r"""^(?:[A-F0-9]{1,4}:){6}(?:[A-F0-9]{1,4}:
            [A-F0-9]{1,4}|(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)
            {3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$""", re.X)
    return ip_regex.match(ip_address)

def verify_ipv4(ip_address):
    """Verifies that the ip is a vaild IPv4 address"""
    ip_regex = re.compile(r"""^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$""", re.X)
    return ip_regex.match(ip_address)

def verify_netmask(net_mask):
    """Verifies that the net mask is vaild"""
    net_regex = re.compile(r"""(?:^(0?[1-9]|[12][0-9]|3[0-2])$)
            |^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$""", re.X)
    return net_regex.search(net_mask)

def convert_netmask(net_mask):
    """Converts a net mask to IPv4"""
    ones = int(net_mask)
    zeros = 32 - ones
    mask = ""
    for one in range(ones):
        if ((one + 1) % 8) == 0:
            mask += "1."
        else:
            mask += "1"
    for _ in range(zeros):
        length = len(mask)
        if length % 9 == 7:
            mask += "0."
        else:
            mask += "0"
    return mask[:35]

def convert_ip_netmask(net_mask):
    """Converts a given net mask in ipv4 to 1s and 0s"""
    numbers = net_mask.split(".")
    mask = ""
    rang = len(numbers)
    for i in range(rang):
        binary = bin(int(numbers[i]))
        string = binary[2:]
        if len(string) != 8:
            zeros = 8 - len(string)
            string += "0" * zeros
        if i < (rang - 1):
            mask += string + "."
        else:
            mask += string
    return mask

def calculate_ipv4_subnet(ip_address, net_mask):
    """Calculates the subnet of an IPv4 address"""
    ip_bits = ip_address.split(".")
    net_bits = net_mask.split(".")
    subnet = ""
    bits = len(ip_bits)
    for bit in range(bits):
        ip_bit = int(ip_bits[bits - 1])
        net_bit = int(net_bits[bits - 1])
        if (bit + 1) % 4 == 0:
            subnet += str((ip_bit & net_bit))
        else:
            subnet += str((ip_bit & net_bit)) + "."
    return subnet
