# Если таблица продуктов на складе. Данные представлены в виде list of dicts
# Найти самые дорогие товары. Количество товаров, которые необходимо вывести 
# будет передано в первом аргументе, данные по товарам будут переданы вторым аргументом.

price_list_1 = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]

price_list_2 = [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]

def bigger_price(amount, price_list):
    return sorted(price_list, key=lambda k: k['price'])[-amount:]


print(bigger_price(2, price_list_1))
print(bigger_price(1, price_list_2))
