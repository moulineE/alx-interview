#!/usr/bin/python3
"""0x08. Making Change"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    :param coins:
    :param total:
    :return:
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    few_num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        few_num_coins += total // coin
        total %= coin
    return few_num_coins if total == 0 else -1
