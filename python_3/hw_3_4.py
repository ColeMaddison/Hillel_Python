# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.

string = 'oellh'

def change_first_last(string):
    return '{}{}{}'.format(string[-1], string[1:-1], string[0])


print(change_first_last(string))