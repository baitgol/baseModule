# -*- coding: utf-8 -*-
from functools import reduce


def log(f):
    def fn(*args, **kw):
        print('call ' + f.__name__ + '()...')
        return f(*args, **kw)
    return fn


# @log
def add(x, y):
    return x + y

f =log(add)
print(f(1, 2))
# print(add(1, 2))


@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))