import itertools
from pprint import pprint
main_matrix = dict()

count = 1
for skip in range(1, 13):
  matrix_a = list()
  for i in range(1, 13):
    for j in range(1, 13):
      for k in range(1, 13):
        if i < j and j < k and i < k and i != skip and j != skip and k != skip:
          matrix_a.append([i, j, k])
  main_matrix[count] = matrix_a
  count += 1

# for key, value in main_matrix.items():
#   print("matrix " + str(key))
#   print(value)
list_of_matrices = list()
for value in main_matrix.values():
  list_of_matrices.append(value)

result = list(itertools.product(*list_of_matrices))
pprint(result)