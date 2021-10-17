# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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

print(f'Чаще всего {dict_[max_item]} раз встречается число {max_item}')
