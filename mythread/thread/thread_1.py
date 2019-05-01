# -*- coding: cp936 -*-
import threading
import time

class mythread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self._num = num

    def run(self): # 重写run函数
        global mutex,count
        threadname = threading.currentThread().getName()
        print('thread %s starting...'%(threadname))
        list_thread = threading.enumerate()
        print(list_thread)
        for i in range(self._num):
            mutex.acquire()# 取得锁
            count = count + 1
            print('thread %s starting...'%(threadname))
            print(count)
            mutex.release() #释放锁
            time.sleep(5)

if __name__ == '__main__':
##    t = mythread()
##    t.start()
##    t.join()  
    global mutex, count, count
    count =1
    threads = []
    mutex = threading.Lock() #创建锁
    num = 3
    for i in range(1,num):
        threads.append(mythread(i))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    





##Thread 表示一个线程的执行的对象
##Lock 锁原语对象（跟thread 模块里的锁对象相同）
##RLock 可重入锁对象。使单线程可以再次获得已经获得了的锁（递归锁定）。
##Condition 条件变量对象能让一个线程停下来，等待其它线程满足了某个“条件”。
##如，状态的改变或值的改变。
##Event 通用的条件变量。多个线程可以等待某个事件的发生，在事件发生后，
##所有的线程都会被激活。
##Semaphore 为等待锁的线程提供一个类似“等候室”的结构
##BoundedSemaphore 与Semaphore 类似，只是它不允许超过初始值
##Timer 与Thread 相似，只是，它要等待一段时间后才开始运行。

##守护进程
##如果你的主线程要退出的时候，不用等待那些子线程完成，那就设定这些线程的daemon 属性
##即，在线程开始（调用thread.start()）之前，调用setDaemon()函数设定线程的daemon 标志
##（thread.setDaemon(True)）就表示这个线程“不重要”

##Thread 对象的函数
##函数 描述
##start() 开始线程的执行
##run() 定义线程的功能的函数（一般会被子类重写）
##join(timeout=None) 程序挂起，直到线程结束；如果给了timeout，则最多阻塞timeout 秒
##getName() 返回线程的名字
##setName(name) 设置线程的名字
##isAlive() 布尔标志，表示这个线程是否还在运行中
##isDaemon() 返回线程的daemon 标志
##setDaemon(daemonic) 把线程的daemon 标志设为daemonic（一定要在调用start()函数前调用）
##activeCount() 当前活动的线程对象的数量
##currentThread() 返回当前线程对象
##enumerate() 返回当前活动线程的列表
##settrace(func)a 为所有线程设置一个跟踪函数
##setprofile(func)a 为所有线程设置一个profile 函数
