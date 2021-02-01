# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

dict = {}
max_item = 0
for item in array:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

    if max_item == 0:
        max_item = item
    elif dict[item] > dict[max_item]:
        max_item = item

print(f'Чаще всего {dict[max_item]} раз встречается число {max_item}')
# print(dict)