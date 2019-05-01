# -*- coding: utf-8 -*-

"""
编写带参数decorator
    标准的decorator：
    def log_decorator(f):
        def wrapper(*args, **kw):
            print('[%s] %s()...' % (prefix, f.__name__))
            return f(*args, **kw)
        return wrapper
再加一层
log(prefix):
    标准
    return
"""
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print('[%s] %s()...' % (prefix, f.__name__))
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def mytest():
    pass
print(mytest())
