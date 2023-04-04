def matrix_divided(matrix, div):
    """checks if matrix are intigers or float"""
    if not isinstance (matrix, (int,float)):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError ("Each row of the matrix must have the same size")
    if not isinstance (div, (int,float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    if
