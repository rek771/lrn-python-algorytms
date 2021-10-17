# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

default_num = ord('a')

dig_1 = ord(input('Введите первую букву от a до z : '))
dig_2 = ord(input('Введите вторую букву от a до z, отличную от первой : '))

place_1 = dig_1 - default_num + 1
place_2 = dig_2 - default_num + 1

digs_between = abs(dig_1 - dig_2) - 1

print(f'{place_1=}')
print(f'{place_2=}')
print(f'{digs_between=}')
