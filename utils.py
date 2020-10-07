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
    return net_regex.match(net_mask)
