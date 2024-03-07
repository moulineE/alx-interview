#!/usr/bin/python3
"""0x09. Island Perimeter module"""
from typing import List


def island_perimeter(grid: List[List]) -> int:
    """
    function that returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    height = len(grid)
    width = len(grid[0])
    perimeter = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
