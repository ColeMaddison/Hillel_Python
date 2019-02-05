# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инсрукций

from contextlib import contextmanager
import time

@contextmanager
def elapsed():
    try:
        start = time.time()
        yield
    finally:
        end = time.time()
        print('Time taken for execusion: {} seconds.'.format(end - start))

with elapsed():
    sum = 0
    for i in range(5000000):
        sum += i