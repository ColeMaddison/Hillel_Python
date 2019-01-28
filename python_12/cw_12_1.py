# check the exceptions

try:
    1 + '42'
except Exception as e:
    caught = e

caught.args # check all data about exception
caught.__traceback__ # get traceback

#or
import traceback
traceback.print_tb(caught)

# raise arrors
raise TypeError('type mismatch')

# raise somrthong - smth must be instance of baseexception
# raise 42 # no

# if type only raise - it will raise last raised exception or if it does not exist - runtimeerro:
# try:
#     some()
# except Exception:       #------- # e is available here
#     raise               #       |
#                         #       |
# def some():             #       |
#     try:                #       |
#         1/0             #       |
#     except Exception as e: #    |
#         print(e)           # ----

# it can be one error after another
# try:
#     {}['f']
# except Exception: # same as finally: - error after error
#     1/0

#метод __enter__ иниц контент (открыв файл захват мьютекс???) знач возвращ __enter__
#запис по имени указанному после оператора as

#метод __exit__ вызыв после выполн тела оператора with метод приним 3 арг (тип искл, само искл, 
# объект типа traceback)

# если в проц исполн тела with было поднято искл - метод __exit__ подавл его возвращая true

# менежер контекста - класс с 2 методами

# def acc():
#     pass

# with acc() as r:
#     do(r)

# import sys
# manager = acc()
# r = manager.__enter__()

# try:
#     do(r)
# finally:
#     exc_type, exc_val, tb = sys.exc_info()
#     suppress = manager.__exit__(exc_type, exc_val, tb)

#     if exc_val is not None and not suppress:
#         raise exc_val


# with can work with many context managers 
# def a():
#     pass
# def b():
#     pass
# def do(a, b):
#     pass


# with a() as a, b() as b:
#     do(a, b)

#mutext - block thread to finish working with it

# import sys
import threading

class synch(object):
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, *exc_info):
        self.lock.release()

# import tempfile # temporary files after  only available in with block


# import os

# class cd:
#     def __init__(self, path):
#         self.path = path
#     def __enter__(self):

    