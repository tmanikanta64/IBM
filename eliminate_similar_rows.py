matrix_a = [
    [2, 3, 5],
    [1, 2, 4],
    [1, 6, 3],
    [2, 4, 6]
]

matrix_b = [
    [2, 3, 5],
    [5, 6, 7],
    [1, 2, 4],
    [1, 6, 3]
]

for a_row in matrix_a:
    for b_row in matrix_b:
        if a_row == b_row:
            matrix_b.remove(b_row)
print(matrix_b)
