# import time
# from functools import wraps
#
# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         r = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end - start)
#         return r
#     return wrapper
#
# @timethis
# def countdown(n):
#     while n > 0:
#         n -= 1
#
# countdown(100000)

from inspect import Signature, Parameter

parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
           Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]

sig = Signature(parms)
print(sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name,value)

func(1, 2, z=3)
func(1)
func(1, z=3)
func(y=2, x=1)
# func(1, 2, 3, 4)