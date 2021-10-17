"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
"""

from timeit import timeit
from cProfile import run


# «Решето Эратосфена» с автоматическим расширением решета
def sieve(n: int):
    n_min = 0
    n_max = 100
    sieve_arr = []
    # sieve_arr = [0,1]

    while True:
        n_now = n
        sieve_arr += [i for i in range(n_min, n_max + 1)]

        for i in range(2, n_max):
            if sieve_arr[i] != 0:
                j = i + i
                while j < n_max + 1:
                    sieve_arr[j] = 0
                    j += i

        for i in sieve_arr:
            if i != 0:
                n_now -= 1

                if n_now == 0:
                    # print(sieve_arr) на случай важного дебага
                    return i

        n_min = n_max + 1
        n_max = n_max + 100


# print(timeit('sieve(10)', number=10, globals=globals()))  # 0.00027309999999999834
# print(timeit('sieve(100)', number=10, globals=globals()))  # 0.0098462
# print(timeit('sieve(1_000)', number=10, globals=globals()))  # 1.1710322

# run('sieve(100)')
# """
#          10 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.001    0.001 2.py:29(sieve)
#         6    0.000    0.000    0.000    0.000 2.py:37(<listcomp>)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# """
#
# run('sieve(1000)')
# """
#          84 function calls in 0.186 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.185    0.185    0.186    0.186 2.py:29(sieve)
#        80    0.001    0.000    0.001    0.000 2.py:37(<listcomp>)
#         1    0.000    0.000    0.186    0.186 <string>:1(<module>)
#         1    0.000    0.000    0.186    0.186 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# """
#
# run('sieve(10000)')
# """
#
#          1052 function calls in 19.291 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1   19.284   19.284   19.291   19.291 2.py:29(sieve)
#      1048    0.007    0.000    0.007    0.000 2.py:37(<listcomp>)
#         1    0.000    0.000   19.291   19.291 <string>:1(<module>)
#         1    0.000    0.000   19.291   19.291 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
#
# """


# обычная функция поиска простых чисел
def prime(n: int):
    if n == 1:
        return 1

    n -= 1
    num = 1

    while True:
        num += 1

        for i in range(2, num + 1):
            if num % i == 0 and i != num:  # не простое
                n += 1
                break

        n -= 1
        if n == 0:
            return num


# print(timeit('prime(10)', number=10, globals=globals()))  # 0.00015010000000000023
# print(timeit('prime(100)', number=10, globals=globals()))  # 0.0157775
# print(timeit('prime(1_000)', number=10, globals=globals()))  # 2.0860626


run('prime(100)')
"""
         4 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.002    0.002 2.py:114(prime)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""

run('prime(1000)')
"""
         4 function calls in 0.217 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.217    0.217    0.217    0.217 2.py:114(prime)
        1    0.000    0.000    0.217    0.217 <string>:1(<module>)
        1    0.000    0.000    0.217    0.217 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

run('prime(10000)')
"""
 Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   36.477   36.477   36.477   36.477 2.py:114(prime)
        1    0.000    0.000   36.477   36.477 <string>:1(<module>)
        1    0.000    0.000   36.477   36.477 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# Вместо выводов:
# Решето срабатывает заметно быстрее, если ищет число в первоначально заданном списке.
# С расширением списка увеличивается и время выполнения, что приближает этот алгоритм к алгоритму без решета
# по времени выполнения. Оба алгоритма, по моему мнению, имеют сложность O(n^2)
# в связи с большим числом вложенных циклов и по результатам замера времени выполнения.


# На случай важного дебага
# print(prime(1))
# print(prime(4))
# print(prime(18))
# print(prime(180))
# print(sieve(1))
# print(sieve(4))
# print(sieve(18))
# print(sieve(180))
