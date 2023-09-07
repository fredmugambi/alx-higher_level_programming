def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = []
    for row in matrix:
        new_row = [round(val / div, 2) for val in row]
        result_matrix.append(new_row)

    return result_matrix
