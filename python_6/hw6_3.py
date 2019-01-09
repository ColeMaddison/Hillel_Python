# Задача-3 - не обязательна к выполнению
# Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.
# Например ваша функция может иметь вид


def decor(func):
    def wrapper():
        try:
            func()
        except:
            print('Error caught!!')
    return wrapper

@decor
def my_func():
    raise ValueError("some text error")

my_func()