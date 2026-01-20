#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def row_copy():
        return row.copy()
    new_matrix = matrix.copy()
    map(lambda row: row_copy(), new_matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = new_matrix[i][j] **2
    return new_matrix
