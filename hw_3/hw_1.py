# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

start_num = 2
end_num = 99
start_dig = 2
end_dig = 9

array = {dig: 0 for dig in range(start_dig, end_dig + 1)}

for number in range(start_num, end_num + 1):
    for dig in range(start_dig, end_dig + 1):
        if number % dig == 0:
            array[dig] += 1

for dig, freq in array.items():
    print(f'Число {dig} кратно {freq} раз в заданном диапазоне от {start_num} до {end_num}.')
