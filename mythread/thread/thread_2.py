#!/usr/bin/python
# -*- coding: cp936 -*-

#threading ģ��2�ַ���
#1. ����ֱ�Ӵ��ݽ�thread����
#-*- encoding: gb2312 -*-
import string, threading, time
 
def thread_main(a):
    global count, mutex
    # ����߳���
    threadname = threading.currentThread().getName()
     
    for x in range(0, int(a)):
        # ȡ����
        mutex.acquire()
        count = count + 1
        # �ͷ���
        mutex.release()
        print(threadname, x, count)
        time.sleep(1)
     
def main(num):
    global count, mutex
    threads = []
     
    count = 1
    # ����һ����
    mutex = threading.Lock()
    # �ȴ����̶߳���
    for x in range(0, num):
        threads.append(threading.Thread(target=thread_main, args=(1,)))
    # ���������߳�
    for t in threads:
        t.start()
    # ���߳��еȴ��������߳��˳�
    for t in threads:
        t.join()  
     
     
if __name__ == '__main__':
    num = 4
    # ����4���߳�
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
##    # ������
##    mutex = threading.Lock()
##    # �����̶߳���
##    for x in xrange(0, num):
##        threads.append(Test(2))
##    # �����߳�
##    for t in threads:
##        t.start()
##    # �ȴ����߳̽���
##    for t in threads:
##        t.join()  

