#!/usr/bin/python3
"""0. UTF-8 Validation module"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    :param data:
    :return: True or False
    """
    try:
        """convert the int to 8 bit with and operator"""
        data = [i & 0xFF for i in data]
        """try to decode"""
        bytes(data).decode('utf-8')
        return True
    except Exception:
        return False
