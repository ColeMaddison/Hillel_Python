# декораторы

# def my_decorator(to_decor):
#     def wrapper(arg):
#         print("before func call")
#         to_decor(arg)
#         print("still in decor")
#     return wrapper


# @my_decorator
# def print_smth(arg):
#     print(arg)

# print_smth("in the func------")

# def momoize(f):
#     cache = {}

#     def wrapper(*args):
#         if(args in cache):
#             print('\nfrom cache')
#             return cache[args]
#         else:
#             print('\ncalled')
#             cache[args] = f(*args)
#             return cache[args]
    
#     return wrapper

# @momoize
# def summar(a, b):
#     return a + b

# print(summar(1,2))
# print(summar(1,2))
# print(summar(1,3))


from functools import partial

def greet(greeting, separator, emphasis, name):
    print(greeting, separator, emphasis, name)

newf = partial(greet, greeting='Hello', separator=',', emphasis='!')

print(newf)