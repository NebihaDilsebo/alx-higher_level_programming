#!/usr/bin/python3
"""defines a pascal triangle function"""


def pascal_triangle(n):
    """represents a pascal triangle of n size"""
    if n < 0:
        return []

    """create the first row"""
    row = [1]
    result = [row]

    """generate the next n-1 rows"""
    for i in range(1, n):
        """cal current row based on previous one"""
        row = [1] + [row[j] + row[j+1] for j in range(i-1)] + [1]
        result.append(row)

        return result
