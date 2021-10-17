# 2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается
# в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование
# встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque


def summ(dnum_1, dnum_2, num_system):
    """
    Суммирует в заданной системе счисления
    :param str|deque dnum_1: 1е число
    :param str|deque dnum_2: 2е число
    :param int num_system: Число, представляющее систему. Например для 16-ти ричной число 16
    :return: сумма в заданной системе счесления
    """
    assert num_system <= 36, 'Не умею считать больше 36'
    dnum_1 = deque(dnum_1)
    dnum_2 = deque(dnum_2)

    if len(dnum_2) > len(dnum_1):
        dnum_1, dnum_2 = dnum_2, dnum_1

    dnum_1.reverse()
    dnum_2.reverse()
    counter = {num: pos for pos, num in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    counter_pos = [num for num in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']  # костыль чтобы получать элемент за О(1)

    res = deque()
    memory = 0

    for i, n1 in enumerate(dnum_1):
        n1 = str(n1)

        n1 = n1.upper()

        if len(dnum_2) < i + 1:
            counter_n2 = 0
        else:
            dnum_2[i] = str(dnum_2[i])
            counter_n2 = counter[dnum_2[i].upper()]

        if counter[n1] + counter_n2 + memory > num_system - 1:
            res.append(counter_pos[(counter[n1] + counter_n2 + memory) % num_system])
            memory = (counter[n1] + counter_n2 + memory) // num_system
        else:
            res.append(counter_pos[counter[n1] + counter_n2 + memory])
            memory = 0

    if memory > 0:
        res.append(counter_pos[memory])

    res.reverse()
    return ''.join(res)


def multt(dnum_1, dnum_2, num_system):
    """
    Умножает в заданной системе счисления
    :param str dnum_1: 1е число
    :param str dnum_2: 2е число
    :param int num_system: Число, представляющее систему. Например для 16-ти ричной число 16
    :return: произведение в заданной системе счесления
    """
    assert num_system <= 36, 'Не умею считать больше 36'

    dnum_1 = deque(dnum_1)
    dnum_2 = deque(dnum_2)

    dnum_1.reverse()
    dnum_2.reverse()

    if len(dnum_2) > len(dnum_1):
        dnum_1, dnum_2 = dnum_2, dnum_1

    counter = {num: pos for pos, num in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    counter_pos = [num for num in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']  # костыль чтобы получать элемент за О(1)

    spam_res = deque()
    res = deque()
    memory = 0
    for i, num1 in enumerate(dnum_1):
        for num2 in dnum_2:
            n1 = num1.upper()
            counter_n2 = counter[num2.upper()]

            if counter[n1] * counter_n2 + memory > num_system - 1:
                spam_res.append(counter_pos[(counter[n1] * counter_n2 + memory) % num_system])
                memory = (counter[n1] * counter_n2 + memory) // num_system
            else:
                spam_res.append(counter_pos[counter[n1] * counter_n2 + memory])
                memory = 0

        if memory > 0:
            spam_res.append(counter_pos[memory])
            memory = 0

        if i != 0:
            spam_res.reverse()

            for _ in range(i):
                spam_res.append('0')

            res = summ(spam_res, res, num_system)
        else:
            res = spam_res
            res.reverse()

        spam_res = deque()

    return ''.join(res)


num_1 = input('Введите 1е число: ')
num_2 = input('Введите 2е число: ')

print(f'Сумма чисел: {summ(num_1, num_2, 16)}')
print(f'Произведение чисел чисел: {multt(num_1, num_2, 16)}')
