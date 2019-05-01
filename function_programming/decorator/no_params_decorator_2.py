# -*- coding: utf-8 -*-

from functools import reduce

"""
编写一个@performance，它可以打印出函数调用的时间。
计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。
"""

import time

def performance(f):
    def g(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' %(f.__name__,t2-t1))
        return r
    return g


@performance
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(1000))
