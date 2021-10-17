# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

# from collections import OrderedDict не используем
# from collections import defaultdict ведёт себя как dict, никакой пользы
from collections import Counter
from collections import deque

count_enterprises = int(input('Введите количество предприятий: '))

enterprises = Counter()
for i in range(count_enterprises):
    name = input(f'Введите название предприятия №{i + 1}: ')
    for j in range(4):
        enterprises[name] += int(input(f'Введите выручку предприятия за {j + 1} квартал: '))

max_values = deque()
min_values = deque()
middle = sum(enterprises.values()) / len(enterprises.items())

print('Вы ввели компании:')

name: str
value: int
for name, value in enterprises.items():
    print(f'{name.title()} c общей выручкой {value} руб.')
    if value > middle:
        max_values.append(name)
    elif value < middle:
        min_values.append(name)
    # если равно среднему видимо по условию не показываем

print(f'Компании со средней выручкой выше среднего ({middle}):')
for name in max_values:
    print(name)

print(f'Компании со средней выручкой ниже среднего ({middle}):')
for name in min_values:
    print(name)

# from collections import namedtuple не придумал как реализовать в задаче :(((((
