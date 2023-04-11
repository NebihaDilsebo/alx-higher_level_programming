#!/usr/bin/python3
"""defines a pascal triangle function"""


def pascal_triangle(n):
    """represents a pascal triangle of n size"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range (1, n):
        prev_row = triangle[-1]
        row = [1] + [prev_row[j] + prev_row[j+1] for j in range(i - 1)] + [1]
        triangle.append(row)

        return triangle
