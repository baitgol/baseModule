#!/usr/bin/python
# -*- coding: cp936 -*-

#threading 模块2种方法
#1. 函数直接传递进thread对象
#-*- encoding: gb2312 -*-
import string, threading, time
 
def thread_main(a):
    global count, mutex
    # 获得线程名
    threadname = threading.currentThread().getName()
     
    for x in range(0, int(a)):
        # 取得锁
        mutex.acquire()
        count = count + 1
        # 释放锁
        mutex.release()
        print(threadname, x, count)
        time.sleep(1)
     
def main(num):
    global count, mutex
    threads = []
     
    count = 1
    # 创建一个锁
    mutex = threading.Lock()
    # 先创建线程对象
    for x in range(0, num):
        threads.append(threading.Thread(target=thread_main, args=(1,)))
    # 启动所有线程
    for t in threads:
        t.start()
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join()  
     
     
if __name__ == '__main__':
    num = 4
    # 创建4个线程
    main(4)

##class Test(threading.Thread):
##    def __init__(self, num):
##        threading.Thread.__init__(self)
##        self._run_num = num
##     
##    def run(self):
##        global count, mutex
##        threadname = threading.currentThread().getName()
##     
##        for x in xrange(0, int(self._run_num)):
##            mutex.acquire()
##            count = count + 1
##            print x,count
##            mutex.release()
##            print threadname
##            time.sleep(1)
## 
##if __name__ == '__main__':
##    global count, mutex
##    threads = []
##    num = 4
##    count = 1
##    # 创建锁
##    mutex = threading.Lock()
##    # 创建线程对象
##    for x in xrange(0, num):
##        threads.append(Test(2))
##    # 启动线程
##    for t in threads:
##        t.start()
##    # 等待子线程结束
##    for t in threads:
##        t.join()  

