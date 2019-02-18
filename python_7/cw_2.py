# *Задача-2*
# Написать декоратор который будет выводить время выполнения вашей функции

import time

def my_decorator(to_decor):
    def wrapper():
        start_time = time.time()
        to_decor()
        print("Time of exec = {}".format(time.time() - start_time))
    return wrapper


@my_decorator
def print_smth():
    return range(1000000000000)

print_smth()