# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Для решения задачи сортировки эти три этапа выглядят так:
#
#     Сортируемый массив разбивается на две части примерно одинакового размера;
#     Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
#     Два упорядоченных массива половинного размера соединяются в один.
#
# 1.1. — 2.1. Рекурсивное разбиение задачи на меньшие происходит до тех пор, пока размер массива не достигнет единицы (любой массив длины 1 можно считать упорядоченным).
#
# 3.1. Соединение двух упорядоченных массивов в один.
# Основную идею слияния двух отсортированных массивов можно объяснить на следующем примере. Пусть мы имеем два уже отсортированных по возрастанию подмассива. Тогда:
# 3.2. Слияние двух подмассивов в третий результирующий массив.
# На каждом шаге мы берём меньший из двух первых элементов подмассивов и записываем его в результирующий массив. Счётчики номеров элементов результирующего массива и подмассива, из которого был взят элемент, увеличиваем на 1.
# 3.4. «Прицепление» остатка.
# Когда один из подмассивов закончился, мы добавляем все оставшиеся элементы второго подмассива в результирующий массив.


from random import random


def merge(arr):
    if len(arr) == 1:
        return arr
    res = [None] * len(arr)

    # Рекурсивно разбиваем и сортируем малые части
    left = merge(arr[len(arr) // 2:])
    right = merge(arr[:len(arr) // 2])

    # В цикле соединяем массивы
    li = ri = 0
    while len(left) > li and len(right) > ri:
        if left[li] > right[ri]:
            res[li + ri] = right[ri]
            ri += 1
        else:
            res[li + ri] = left[li]
            li += 1

    # Добавляем "хвост" который мог остаться если left и right не равны по длинне
    while len(left) > li:
        res[li + ri] = left[li]
        li += 1

    while len(right) > ri:
        res[li + ri] = right[ri]
        ri += 1

    return res


MIN_NUM = 0
MAX_NUM = 49
COUNT_NUM = 10

array = [(MAX_NUM - MIN_NUM) * random() + MIN_NUM for _ in range(COUNT_NUM)]

print(array)
array = merge(array)
print(array)