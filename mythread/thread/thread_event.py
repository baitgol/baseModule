#coding:utf-8

import threading

class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name = threadname)

    def run(self):
        global  event
        if event.isSet():         #判断是否为空
            event.clear()          #设置为假
            print 'c'+self.getName()
            event.wait()           #为真立即执行
            print self.getName()

        else:
            print self.getName()
            event.set()


event = threading.Event()
event.set()       #设置 event为真
t1 = []
for i in range(4):
    t= mythread(str(i))
    t1.append(t)

for i in t1:
    i.start()
    

