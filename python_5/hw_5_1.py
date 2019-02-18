# LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не 
# запрашивались. Соответственно, необходимо хранить время последнего запроса к значению. И как только 
# число закэшированных значений превосходит N необходимо вытеснить из кеша значение, которое дольше всего 
# не запрашивалось.
#
# Задача - 1
# Создать декоратор lru_cache(подобный тому который реализован в Python).
#
# Задача-2
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_info  - статистика использования вашего кеша(например: сколько раз вычислялась ваша функция,
# а сколько раз значение было взято из кеша, сколько места свободно в кеше)
#
# Задача-3
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_clear - очищает кеш

from collections import OrderedDict
from functools import wraps

def lru_cache(max_size, typed):
    def decor(my_func):
        cache = OrderedDict()
        info = {'hits': 0, 'misses': 0}
        @wraps(my_func)
        def wrapper(arg):
            if arg in cache:
                print('from cache')
                info['hits'] += 1
                return cache[arg]
            else:
                if not max_size or (max_size and len(cache) < max_size):
                    print('from func call in cache range')
                    info['misses'] += 1
                    cache[arg] = my_func(arg)
                    return my_func(arg)
                else: 
                    print('from func call, cache modified')
                    info['misses'] += 1
                    cache.popitem(0)
                    cache[arg] = my_func(arg)
                    # print([*cache.keys()])
                    return my_func(arg)

        def cache_info():
            print('CacheInfo: hits = {}, misses = {}, max size = {}, current size = {}'\
                .format(info['hits'], info['misses'], max_size, len(cache)))
        
        wrapper.cache_info = cache_info
        def cache_clear():
            cache.clear()
            print('Cache cleared')

        wrapper.cache_clear = cache_clear
        return wrapper
    return decor

@lru_cache(max_size = 2, typed = False)
def my_func(arg):
    return arg + 1


my_func(1)
my_func(1)
my_func(2)
my_func(2)
my_func(3)
my_func.cache_info()
my_func.cache_clear()
my_func(3)
my_func.cache_info()



# my_func.cache_clear()
