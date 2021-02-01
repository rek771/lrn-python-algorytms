# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE_N = 3
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
print(*matrix, sep='\n')

min_in_col = 0
max_in_min = 0

for row in range(len(matrix[0])):
    for col in range(len(matrix)):
        if col == 0 or matrix[col][row] < min_in_col:
            _min_in_col = matrix[col][row]

    if max_in_min < min_in_col:
        max_in_min = min_in_col

print(max_in_min)
