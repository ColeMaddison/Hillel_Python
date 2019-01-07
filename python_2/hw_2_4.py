# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве, с индексом n. Если n за границами массива, тогда вернуть -1.

array = [1, 2, 10, 46, 16]
n = 3

def find_elem(array, n):
    if(n > len(array) or n < 0):
        print('here')
        return -1
    return pow(array[n-1], n)
    
print(find_elem(array, n))