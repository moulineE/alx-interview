#!/usr/bin/python3
"""0x05. N Queens task"""
import sys


def nqueens(n: int):
    """solves the N queens problem"""
    print(n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    nqueens(n)
