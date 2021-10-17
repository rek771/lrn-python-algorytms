# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
# замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрана задача из 3го урока #4 "Определить, какое число в массиве встречается чаще всего."

from timeit import timeit
from cProfile import run
import random


# для 1го случая был выбран мой вариант со словарем (к слову, у Вас он тоже присутствовал)
def finder1(size: int):
    min_item = 0
    max_item = 1_000_000
    array = [random.randint(min_item, max_item) for _ in range(size)]

    dict_ = {}
    max_item = 0
    for item in array:
        if item in dict_:
            dict_[item] += 1
        else:
            dict_[item] = 1

        if max_item == 0:
            max_item = item
        elif dict_[item] > dict_[max_item]:
            max_item = item
    return dict_[max_item], max_item


# print(timeit('finder1(10)', number=100, globals=globals()))  # 0.009964200000000006
# print(timeit('finder1(100)', number=100, globals=globals()))  # 0.08732259999999997
# print(timeit('finder1(1000)', number=100, globals=globals()))  # 0.7069328
# print(timeit('finder1(10000)', number=100, globals=globals()))  # 4.7064274

# По времени выполнения могу предположить, что алгоритм имеет линейную сложность.
# Тем не менне увеличение времени выполнения от числа элементов не совсем линейно, что я списываю на погрешность
# вычислений.

# run('finder1(10)')
"""
56 function calls in 0.001 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 1.py:19(finder1)
        1    0.000    0.000    0.001    0.001 1.py:22(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
       10    0.000    0.000    0.001    0.000 random.py:200(randrange)
       10    0.000    0.000    0.001    0.000 random.py:244(randint)
       10    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

# run('finder1(100)')
"""

         511 function calls in 0.001 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 1.py:19(finder1)
        1    0.000    0.000    0.001    0.001 1.py:22(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      100    0.000    0.000    0.001    0.000 random.py:200(randrange)
      100    0.000    0.000    0.001    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      106    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

# run('finder1(1000)')
"""

         5055 function calls in 0.010 seconds
      Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.010    0.010 1.py:19(finder1)
        1    0.001    0.001    0.009    0.009 1.py:22(<listcomp>)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
     1000    0.003    0.000    0.006    0.000 random.py:200(randrange)
     1000    0.002    0.000    0.007    0.000 random.py:244(randint)
     1000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1050    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         50481 function calls in 0.100 seconds
"""

# run('finder1(10000)')
"""       
50481 function calls in 0.100 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.014    0.014    0.099    0.099 1.py:19(finder1)
        1    0.012    0.012    0.085    0.085 1.py:22(<listcomp>)
        1    0.001    0.001    0.100    0.100 <string>:1(<module>)
    10000    0.030    0.000    0.058    0.000 random.py:200(randrange)
    10000    0.015    0.000    0.073    0.000 random.py:244(randint)
    10000    0.020    0.000    0.028    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.100    0.100 {built-in method builtins.exec}
    10000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10476    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}

"""


# По выводу cProfile вижу, что алгоритм имеет сложность O(2n) в связи с тем, что вначале элементы добавляются в цикле,
# а потом происходит проверка по условию. Собственно, как оказалось, операция randint занимает больше всего времени.


# для второго случая взял пример преподавателя(Ваш) и прогнал с теми же значениями
def finder2(size: int):
    min_item = 0
    max_item = 1_000_000
    array = [random.randint(min_item, max_item) for _ in range(size)]

    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    return frequency, num


# print(timeit('finder2(10)', number=100, globals=globals()))  # 0.010421199999999992
# print(timeit('finder2(100)', number=100, globals=globals()))  # 0.21629310000000002
# print(timeit('finder2(1000)', number=100, globals=globals()))  # 15.970292500000001
# print(timeit('finder2(10000)', number=100, globals=globals()))  # n/a (слишком долго), по рассчетам 1200с или 20 минут

# По времени выполнения предполагаю, что алгоритм имеет O(n^2) квадратичную сложность, о чем говорят первые 3 замера.


run('finder2(10)')
"""
66 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 1.py:134(finder2)
        1    0.000    0.000    0.000    0.000 1.py:137(<listcomp>)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

run('finder2(100)')
"""
611 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 1.py:134(finder2)
        1    0.000    0.000    0.000    0.000 1.py:137(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      105    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

run('finder2(1000)')
"""
6057 function calls in 0.061 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.059    0.059    0.061    0.061 1.py:134(finder2)
        1    0.000    0.000    0.002    0.002 1.py:137(<listcomp>)
        1    0.000    0.000    0.061    0.061 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.061    0.061 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1051    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


# По данным выводам так же видно, что основное время происходит генерация данных при помощи randint


# для 3го случая был выбран первый вариант со словарем, оптимизирована генерация массива,
# а так же я отказался от randint в пользу старого доброго random
def finder3(size: int):
    min_gen_item = 0
    max_gen_item = 1_0

    dict_ = {}
    max_item = 0
    for _ in range(size):
        item = int((max_gen_item - min_gen_item) * random.random() + min_gen_item)
        # print(item) на случай важных тестов
        if item in dict_:
            dict_[item] += 1
        else:
            dict_[item] = 1

        if max_item == 0:
            max_item = item
        elif dict_[item] > dict_[max_item]:
            max_item = item

    return dict_[max_item], max_item


# print(finder3(10))  на случай важных тестов

# print(timeit('finder3(10)', number=100, globals=globals()))  # 0.0006940999999999961
# print(timeit('finder3(100)', number=100, globals=globals()))  # 0.0068632
# print(timeit('finder3(1000)', number=100, globals=globals()))  # 0.047188999999999995
# print(timeit('finder3(10_000)', number=100, globals=globals()))  # 0.44588989999999995
# print(timeit('finder3(100_000)', number=100, globals=globals()))  # 4.48101

# В 3м варианте даже удалось посчитать значения для 100_000 элементов
# + в целом видна положительная тенденция по скорости. Сам алгоритм стремится к O(n) сложности
# с некоторой погрешностью на малых цифрах

# run('finder3(1_000)')
"""
         1004 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 1.py:248(finder3)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
"""

# run('finder3(10_000)')
"""
         10004 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    0.007    0.007 1.py:248(finder3)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects}
"""

# run('finder3(100_000)')
"""
         100004 function calls in 0.071 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.062    0.062    0.071    0.071 1.py:248(finder3)
        1    0.000    0.000    0.071    0.071 <string>:1(<module>)
        1    0.000    0.000    0.071    0.071 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   100000    0.008    0.000    0.008    0.000 {method 'random' of '_random.Random' objects}
"""

# сократилось количество вызовов внешних функций, что, как мы видели раньше, привело к ускорению работы алгоритма


# Выводы:
# Лучше всего показал себя 3й алгоритм засчет того, что он изначально писался как оптимизированная версия
# алгоритмов 1 и 2. В нем сокращено количество вызовов каких либо функций, а так же все вычисления помещены в
# один цикл, что делает сложность алгоритма ближе к линейной.
