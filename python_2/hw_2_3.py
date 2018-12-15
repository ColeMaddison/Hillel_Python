# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

from functools import reduce

number = 123405

# def count_prod(number):
#     return reduce((lambda x, y: (int(x) * int(y))), list(filter(lambda i: int(i)!=0, str(number))))

def count_prod(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

print(count_prod(number))