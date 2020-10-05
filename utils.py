#!/usr/bin/env python3
"""
Provides utility method for bitwises-Add
"""
import re

def is_valid_IP(ip):
    if ip is None:
        raise ValueError('IP Adress cannot be None.')
    ip_regex = re.compile(r'[25[0-5]|2[0-4][0-9]|1[0-9]{2}|0?[0-9]{1,2}\.]{3}[25[0-5]|2[0-4][0-9]|1[0-9]{2}|0?[0-9]{1,2}]')
    if ip_regex.match(ip):
        print("Real")
