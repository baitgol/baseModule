# -*- coding: utf-8 -*-

import time, functools
from functools import reduce

"""
if comment @functools.wraps(f) will print wraps
if not will print factorial
"""

def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial.__name__)


