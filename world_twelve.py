import itertools

main_matrix = dict()
count = 0
for skip in range(1, 13):
    matrix_a = []
    for i in range(1, 13):
        for j in range(1, 13):
            for k in range(1, 13):
                if i < j and j < k and i < k and skip != i and skip != j and skip != k:
                    count += 1
                    matrix_a.append([i, j, k])
    main_matrix[skip] = matrix_a

# print(main_matrix)
# print(main_matrix[2])
# print(count)

# # elimination of like rows ??
# for i in range(1, 13):
#         if i != 1:
#             for key, value in main_matrix.items():
#                 matrix_a = main_matrix[1]
#                 matrix_b = main_matrix[i]
#                 # print(matrix_a)
#                 # print()
#                 # print(matrix_b)
#                 for a_row in matrix_a:
#                     for b_row in matrix_b:
#                         if a_row == b_row:
#                             matrix_b.remove(b_row)

# for key, value in main_matrix.items():
#     print("matrix " + str(key))
#     print(len(value))
#     print(value)

list_of_matrices = list()
list_of_matrices.append(main_matrix[1])
list_of_matrices.append(main_matrix[2])

result = list(itertools.product(*list_of_matrices))
reduced_combinations = list()
# for i in result:
#     print(type(i))
#     break

for i in result:
    if i[0] != i[1]:
        reduced_combinations.append(i)

# print(len(reduced_combinations))
third_matrix = main_matrix[3]
reduced_combinations_v2 = list()
for i in reduced_combinations:
    for j in third_matrix:
        if i[0] != j and i[1] != j:
            reduced_combinations_v2.append([i[0], i[1], j])

fourth_matrix = main_matrix[4]
reduced_combinations_v3 = list()
for i in reduced_combinations_v2:
    for j in fourth_matrix:
        if i[0] != j and i[1] != j and i[2] != j:
            reduced_combinations_v3.append([i[0], i[1], i[2], j])

print(len(reduced_combinations_v3))
