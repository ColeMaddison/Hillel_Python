# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инсрукций

from contextlib import contextmanager
import time

@contextmanager
def elapsed():
    try:
        start = time.time()
        yield
    except Exception as e:
        end = time.time()
        print('Script executed with error {}.'.format(str(e)))
        print('Time taken for execusion: {} seconds.'.format(end - start))
    else: # if no exception is expected, else can be changed to finally
        end = time.time()
        print('Time taken for execusion: {} seconds.'.format(end - start))

with elapsed():
    sum = 0
    for i in range(5000000):
        sum += i
    # raise Exception("error")