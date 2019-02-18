# *Задача -4*

# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию. 
# Если это int, тогда выполнить функцию и вывести результат, если это str(), тогда зарейзить ошибку ValueError 
# (raise ValueError(“string type is not supported”))


# def my_decorator(to_decor):
#     def wrapper(x):
#         if isinstance(x, int):
#             print(x)
#         elif isinstance(x, str):
#             raise ValueError("string type is not supported")
#         to_decor(x)
#     return wrapper


# @my_decorator
# def print_smth(x):
#     return x

# print_smth(2)
# print_smth('2')

from functools import singledispatch


@singledispatch
def print_smth(arg):
    print(arg)

@print_smth.register(str)
def _(arg):
    raise ValueError("string type is not supported")


# print_smth(2)
print_smth('2')