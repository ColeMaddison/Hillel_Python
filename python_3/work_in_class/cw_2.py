# Дан массив чисел (float или int). Вам нужно найти разницу между самым большим 
# максимум) и самым малым (минимум) элементом. Ваша функция должна уметь работать 
# с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).

num_arr_1 = [1, 10, 14, 146, 35, 4, -5]
num_arr_2 = [4]
num_arr_3 = []

# def get_diff(arr):
#     if not arr: 
#         return 0
#     return max(arr) - min(arr)

# print(get_diff(num_arr))

def get_diff(*args):
    if not args:
        return 0
    for arg in args:
        if len(arg):
            print(max(arg) - min(arg))
        else:
            print(0)


get_diff(num_arr_1, num_arr_2, num_arr_3)