"""
4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
4.1) убрать из него повторяющиеся элементы
4.2) вывести 3 наибольших числа из исходного массива 
4.3) вывести индекс минимального элемента массива
4.4) вывести исходный массив в обратном порядке
"""

sample_arr = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

# 4.1 
def remove_identical_1(sample_arr):
    out_arr = []
    for item in sample_arr:
        if item not in out_arr:
            out_arr.append(item) 

    return out_arr

# этот я немного подсмотрел, но он гениален

def remove_identical_2(sample_arr):
    return [item for index, item in enumerate(sample_arr) if item not in sample_arr[:index]]

# print(remove_identical_1(sample_arr))
# print(remove_identical_2(sample_arr))

# --------------------

# 4.2
def get_3_max_1(sample_arr):
    return sorted(sample_arr)[-3:]

# print(get_3_max_1(sample_arr))

# --------------------

# 4.3
def get_min_item_1(sample_arr):
    return sample_arr.index(sorted(sample_arr)[0])

def get_min_item_2(sample_arr):
    return sample_arr.index(min(sample_arr))

def get_min_item_3(sample_arr):
    return [index for (index, item) in enumerate(sample_arr) if item == min(sample_arr)][0]

# print(get_min_item_1(sample_arr))
# print(get_min_item_2(sample_arr))
# print(get_min_item_3(sample_arr))

# --------------------

# 4.4

def get_reverse_arr_1(sample_arr):
    return list(reversed(sample_arr))

def get_reverse_arr_2(sample_arr):
    return sample_arr[::-1]

def get_reverse_arr_3(sample_arr):
    sample_arr.reverse()
    return sample_arr

print(get_reverse_arr_1(sample_arr))
print(get_reverse_arr_2(sample_arr))
print(get_reverse_arr_3(sample_arr))

