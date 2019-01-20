# *Задача-1*
# Написать декоратор который выводит сообщение до вызова функции и после вызова функции

def my_decorator(to_decor):
    def wrapper():
        print("before func call")
        to_decor()
        print("still in decor")
    return wrapper


@my_decorator
def print_smth():
    print("INSIDE")

print_smth()