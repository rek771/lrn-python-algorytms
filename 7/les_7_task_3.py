# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#     Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import random


def mediana(array):
    for num in array:
        more = less = equals = 0

        for compared_num in array:
            if compared_num < num:
                less += 1
            elif compared_num > num:
                more += 1
            else:
                equals += 1

        equals -= 1  # тк само число равно самому себе

        if more == less or more + equals == less or more == less + equals \
                or abs(more - less) < equals:  # если много одинаковых цифр в середине, то они тоже считаются медианой(точнее одно из них)
            return num


MIN_NUM = 0
MAX_NUM = 100

user_num = int(input('Введите длину массива:'))

arr = [int((MAX_NUM - MIN_NUM) * random() + MIN_NUM) for _ in range(user_num * 2 - 1)]

print(arr)

print(f'Медиана = {mediana(arr)}')
