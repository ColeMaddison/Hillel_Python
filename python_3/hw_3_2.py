# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.

from functools import reduce

arr = [1, 3, 45, 65, 12, 9, 6]

# solution 1
def get_mult_1(arr):
    return sum([x for x in arr if arr.index(x)%2 == 0]) * arr[-1]

# solution 2
def get_mult_2(arr):
    return sum(arr[::2]) * arr[-1]

print(get_mult_1(arr))
print(get_mult_2(arr))