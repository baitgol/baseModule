# -*- coding: cp936 -*-
import threading
import time
class mythread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self._num = num

    def run(self): # ��дrun����
        global mutex,count
        threadname = threading.currentThread().getName()
        print 'thread %s starting...'%(threadname)
        list_thread = threading.enumerate()
        print list_thread
        for i in range(self._num):
            mutex.acquire()# ȡ����
            count = count + 1
            print 'thread %s starting...'%(threadname)
            print count
            mutex.release() #�ͷ���
            time.sleep(5)

if __name__ == '__main__':
##    t = mythread()
##    t.start()
##    t.join()  
    global mutex,count,con
    count =1
    threads = []
    mutex = threading.Lock() #������
    num = 3
    for i in range(1,num):
        threads.append(mythread(i))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    




##Thread ��ʾһ���̵߳�ִ�еĶ���
##Lock ��ԭ����󣨸�thread ģ�������������ͬ��
##RLock ������������ʹ���߳̿����ٴλ���Ѿ�����˵������ݹ���������
##Condition ����������������һ���߳�ͣ�������ȴ������߳�������ĳ������������
##�磬״̬�ĸı��ֵ�ĸı䡣
##Event ͨ�õ���������������߳̿��Եȴ�ĳ���¼��ķ��������¼�������
##���е��̶߳��ᱻ���
##Semaphore Ϊ�ȴ������߳��ṩһ�����ơ��Ⱥ��ҡ��Ľṹ
##BoundedSemaphore ��Semaphore ���ƣ�ֻ��������������ʼֵ
##Timer ��Thread ���ƣ�ֻ�ǣ���Ҫ�ȴ�һ��ʱ���ſ�ʼ���С�

##�ػ�����
##���������߳�Ҫ�˳���ʱ�򣬲��õȴ���Щ���߳���ɣ��Ǿ��趨��Щ�̵߳�daemon ����
##�������߳̿�ʼ������thread.start()��֮ǰ������setDaemon()�����趨�̵߳�daemon ��־
##��thread.setDaemon(True)���ͱ�ʾ����̡߳�����Ҫ��

##Thread ����ĺ���
##���� ����
##start() ��ʼ�̵߳�ִ��
##run() �����̵߳Ĺ��ܵĺ�����һ��ᱻ������д��
##join(timeout=None) �������ֱ���߳̽������������timeout�����������timeout ��
##getName() �����̵߳�����
##setName(name) �����̵߳�����
##isAlive() ������־����ʾ����߳��Ƿ���������
##isDaemon() �����̵߳�daemon ��־
##setDaemon(daemonic) ���̵߳�daemon ��־��Ϊdaemonic��һ��Ҫ�ڵ���start()����ǰ���ã�
##activeCount() ��ǰ����̶߳��������
##currentThread() ���ص�ǰ�̶߳���
##enumerate() ���ص�ǰ��̵߳��б�
##settrace(func)a Ϊ�����߳�����һ�����ٺ���
##setprofile(func)a Ϊ�����߳�����һ��profile ����
