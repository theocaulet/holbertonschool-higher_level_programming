#!/usr/bin/python3
"""Module that generates Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle"""
    if n <= 0:
        return []
    triangle = []
    for row in range(n):
        if row == 0:
            line = [1]
        else:
            line = [1]
            for col in range(1, row):
                line.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
            line.append(1)
        triangle.append(line)
    return triangle
