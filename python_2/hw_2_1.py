#1)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# ------------------

from pprint import pformat

#1.1) отсортировать массив из словарей по значению ключа ‘age'

# solution 1
def list_sort_age_1(data):
    return sorted(data, key=lambda item: item['age'])

# solution 2
def list_sort_age_2(data):
    data.sort(key=lambda item: item['age'])
    return data

print(pformat(list_sort_age_1(data)), '\n')
print(pformat(list_sort_age_2(data)))
print('------------------------')

# -------------------

#1.2) сгруппировать данные по значению ключа 'city'

from itertools import groupby

def list_group_city(data):
    list_groupped = []
    data.sort(key=lambda item: item['city'])
    for key, group in groupby(data, lambda x: x['city']):
        group_condition = list({k: i[k] for k in i.keys() if not k == 'city'} for i in group)
        list_groupped.append({key: group_condition})
    return list_groupped

print(pformat(list_group_city(data)))
