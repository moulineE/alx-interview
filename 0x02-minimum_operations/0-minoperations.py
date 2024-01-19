#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    Args:
        n (int): number of H characters to print
    Returns:
        int: fewest number of operations needed
    """
    op = 0
    i = 1
    while i < n:
        if n % i == 0:
            tmp = i
            op += 2
            i += tmp
        else:
            i += tmp
            op += 1
    return op
