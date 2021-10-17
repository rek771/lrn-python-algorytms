# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if a < b < c or c < b < a:
    middle = b
elif a < c < b or b < c < a:
    middle = c
else:
    middle = a

print(f'Среднее число {middle}')
