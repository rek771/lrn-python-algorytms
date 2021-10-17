# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def counter(sequence, dig):
    res = 0
    if sequence % 10 == dig:
        res = 1
    if sequence - 10 < 0:
        return res
    else:
        return res + counter(sequence // 10, dig)


sequence_usr = int(input('Введите последовательность целых чисел: '))
dig_usr = int(input('Введите искомую цифру: '))
count = counter(sequence_usr, dig_usr)

print(f'{count=}')
