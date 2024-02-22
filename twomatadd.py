def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix1[0])):
            row_result.append(matrix1[i][j] + matrix2[i][j])
        result.append(row_result)
    return result

matrix_a = [
    [2, 4, 6, 8],
    [1, 3, 5, 7]
]

matrix_b = [
    [8, 6, 4, 2],
    [7, 5, 3, 1]
]

result_matrix = add_matrices(matrix_a, matrix_b)

print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nSum of Matrices A and B:")
for row in result_matrix:
    print(row)
