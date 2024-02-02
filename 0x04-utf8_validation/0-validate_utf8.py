#!/usr/bin/python3
"""0. UTF-8 Validation module"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    :param data:
    :return: True or False
    """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode('utf-8')
        return True
    except Exception:
        return False
