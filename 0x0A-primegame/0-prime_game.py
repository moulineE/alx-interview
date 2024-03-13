#!/usr/bin/python3
"""0x0A. Prime Game module"""


def isWinner(x: int, nums):
    """Prime Game function"""
    if not nums or x < 1 or x != len(nums):
        return None
    ben = 0
    maria = 0
    primes = sieve_of_eratosthenes(max(nums) + 1)
    for n in nums:
        if n in primes:
            ben += 1
        else:
            maria += 1
    if ben == maria:
        return None
    return "Maria" if maria > ben else "Ben"


def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p]):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers
