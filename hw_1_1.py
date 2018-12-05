"""
1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
"""

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# method №1
def generate_dict_1(keys):
    out_dict = {}
    for i in range(0, len(keys)):
        out_dict[keys[i]] = keys[i]*keys[i]
    return out_dict 

# method №2
def generate_dict_2(keys):
    return dict(zip(keys, [i*i for i in keys]))

# method №3
def generate_dict_3(keys):
    return dict(zip(keys, list(map(lambda x: x*x, keys))))

# method №4
def generate_dict_4(keys):
    return {k: k*k for k in keys}

print(generate_dict_1(keys))
print(generate_dict_2(keys))
print(generate_dict_3(keys))
print(generate_dict_4(keys))