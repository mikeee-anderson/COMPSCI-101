def matrix_addition(matrix1, matrix2):
    # Check if both matrices have the same number of rows and columns
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        print("Incorrect Dimensions!")
        return -1

    # Initialize the result matrix
    result_matrix = []

    # Iterate through the rows and columns to compute the sum
    for row1, row2 in zip(matrix1, matrix2):
        result_row = []
        for val1, val2 in zip(row1, row2):
            result_row.append(val1 + val2)
        result_matrix.append(result_row)

    return result_matrix