#!/usr/bin/python3
"""
a function that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Args:
        n: number of rows
    Returns:
        a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            row.append(factorial(i)//(
                    factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
