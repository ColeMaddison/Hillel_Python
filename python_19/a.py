# Написать функцию которая принимает целое число и преобразует его в римскую систему счета

ROMANS = (('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1))

res = []

def convert(num, res, divider = 10):
    diff = num % divider
    
    for i in ROMANS:
        if i[1] == diff:
            res = [i[0]] + res
            break
        elif i[1] < diff:
            res = [i[0]] + res
            num -= i[1]
            return convert(num, res, divider)

    num = num - diff
    if num == 0: 
        return ''.join(res)
        
    divider *= 10

    return convert(num, res, divider)

print(convert(103, res))