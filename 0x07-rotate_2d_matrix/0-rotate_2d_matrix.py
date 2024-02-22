#!/usr/bin/python3
"""0x07. Rotate 2D Matrix module"""


def rotate_2d_matrix(matrix):
    """function that rotate a 2d matrix by 90°"""
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[n - 1 - j][i]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]
