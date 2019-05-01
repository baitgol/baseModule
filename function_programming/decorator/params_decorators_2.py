# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from functools import reduce

"""
编写一个带参数的@performance，它可以打印出函数调用的时间。
请给 @performace 增加一个参数，允许传入’s’或’ms’
计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。
"""

import time

def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f%s' %(f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator


@performance("ms")
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(10000))
