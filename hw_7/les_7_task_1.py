# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import random


def bubble(array):
    n = 1

    while n < len(array):
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1


MIN_NUM = -100
MAX_NUM = 99
COUNT_NUM = 10

arr = [int((MAX_NUM - MIN_NUM) * random() + MIN_NUM) for _ in range(COUNT_NUM)]

print(arr)
bubble(arr)
print(arr)
