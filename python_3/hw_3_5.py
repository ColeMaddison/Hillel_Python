# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises'

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

def tuple_to_string(tup):
    return ''.join(tup)

print(tuple_to_string(tup))