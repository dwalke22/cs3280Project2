#!/usr/bin/env python3
"""
Provides utility method for bitwises-Add
"""
import re

def verify_ipv6(ip):
    """Verifies that the ip is a valid IPv6 address"""
    if ip is None:
        raise ValueError('IP Adress cannot be None.')
    ip_regex = re.compile(r'^(?:[A-F0-9]{1,4}:){6}(?:[A-F0-9]{1,4}:[A-F0-9]{1,4}|(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$')
    if ip_regex.match(ip):
        print("Real")

def verify_ipv4(ip):
    """Verifies that the ip is a vaild IPv4 address"""
    if ip is None:
        raise ValueError('IP Adress cannot be None.')
    ip_regex = re.compile(r'[25[0-5]|2[0-4][0-9]|1[0-9]{2}|0?[0-9]{1,2}\.]{3}[25[0-5]|2[0-4][0-9]|1[0-9]{2}|0?[0-9]{1,2}]')
    if ip_regex.match(ip):
        print("Real")
