"""
2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только 
четные числа.
"""

# method №1
def generate_list_1():
    return [i for i in range(0, 100) if i%2==0]

# method №2
def generate_list_2():
    return list(filter(lambda x: x%2 == 0, range(0,100)))

print(generate_list_1())
print(generate_list_2())