# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


from random import random

a = int(input('Первое целое число: '))
b = int(input('Второе целое число: '))

if a > b:
    min_num = b
    max_num = a
else:
    min_num = a
    max_num = b

res1 = int((max_num - min_num) * random() + min_num)

a = float(input('Первое вещественное число: '))
b = float(input('Второе вещественное число: '))

if a > b:
    min_num = b
    max_num = a
else:
    min_num = a
    max_num = b

res2 = float((max_num - min_num) * random() + min_num)

a = ord(input('Первая буква: '))
b = ord(input('Вторая буква: '))

if a > b:
    min_num = b
    max_num = a
else:
    min_num = a
    max_num = b

res3 = chr(int((max_num - min_num) * random() + min_num))

print(f'{res1}')
print(f'{res2}')
print(f'{res3}')
