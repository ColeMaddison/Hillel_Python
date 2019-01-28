# Задача-4 - не обязательна к выполнению
# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента

def decor_with_args(*dargs):
    def decor(func):
        def wrapper():
            try:
                func()
            except (dargs):
                print('Oh no')
            else:
                print('Some other error!')
        return wrapper
    return decor


@decor_with_args(ValueError)
def mistakes():
    raise ValueError('mistakes')

mistakes()