"""
5) Найти общие ключи в двух словарях:
dict_one = { ‘a’: 1, ‘b’: 2, ‘c’: 3, ‘d’: 4 }
dict_two = { ‘a’: 6, ‘b’: 7, ‘z’: 20, ‘x’: 40 }
"""

dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40 }

def get_identical_keys_1(dict_one, dict_two):
    return {key: value for key, value in dict_one.items() if key in dict_two}

print(get_identical_keys_1(dict_one, dict_two))