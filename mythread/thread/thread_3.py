#coding:utf-8

import threading
import time


class mythread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        x = 0
        time.sleep(5)
        print(self.id)

def func():
    t.start()
    print(t.isAlive()) #查看线程状态
    t.join()  #等待线程完成
    #print t.isAlive()
    for i in range(5):
        print(i)

t = mythread(2)
func()


