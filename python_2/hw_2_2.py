# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в 
# последовательности.

list_var = ['a', 'a', 'bi', 'bi', 'bi']

def most_frequent(list_var):
    return max([(item, list_var.count(item)) for item in set(list_var)], key=lambda i:i[1])[0]

print(most_frequent(list_var))
