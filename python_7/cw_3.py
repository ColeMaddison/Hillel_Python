# *Задача-3*
# Написать декоратор который будет расширять(добавлять) аргументы к вашей функции.


def my_decorator(to_decor):
    def wrapper(*args, **kwargs):
        print("args?")
        print(args)
        print(kwargs)
        print("end args!")
        to_decor(*args, **kwargs)
    return wrapper


@my_decorator
def print_smth(x):
    return x

print_smth(1)
