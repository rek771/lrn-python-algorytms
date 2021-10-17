# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# задаю минимальный и максимальный индекс равные 1му элементу, чтобы не было лишних проверок в цикле
min_index = 0
max_index = 0

for i, item in enumerate(array):
    if item < array[min_index]:
        min_index = i
    if item > array[max_index]:
        max_index = i

summ = 0
for i in range(min_index + 1, max_index):
    summ += array[i]

print(
    f'Минимальный элемент под индексом {min_index}, а максимальный под индексом {max_index}. Сумма между ними - {summ}.')
