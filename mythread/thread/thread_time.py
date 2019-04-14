import threading
import time

def func(a,b):
    print(time.ctime(),'hello ',a,b)
#Timer(interval,fuction,args=[],kwargs={})
args = [1,2]
print(time.ctime())
timer = threading.Timer(5,func,args)
timer.start()
