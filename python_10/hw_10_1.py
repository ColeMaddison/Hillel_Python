# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем
import os

def check_line(file):
    accum = {}
    for line in open(file):
        if line.strip() not in accum:
            yield line
            accum[line.strip()] = True


for line in check_line('{}/python_10/hw_10_1.txt'.format(os.getcwd())):
    print(line)
