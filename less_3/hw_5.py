# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10_000
MIN_ITEM = -100_000_000
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

max_min_item_index = 0

for i, item in enumerate(array):
    if item < 0:
        if max_min_item_index == 0 or item > array[max_min_item_index]:
            max_min_item_index = i

print(f'Максимальное минимальное число {array[max_min_item_index]}')
