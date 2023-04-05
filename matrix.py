def matrix_divided(matrix, div):
    """checks if matrix is a list of lists of integer or floats"""
    if not all (isinstance (row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    """checks if all rows have the same size
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError ("Each row of the matrix must have the same size")
    if not isinstance (div, (int,float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    return [[round(nb/ div, 2) for nb in row] for row in matrix]
