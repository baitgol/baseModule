# -*- coding: cp936 -*-
import threading    
import time  
  
class Producer(threading.Thread):  
    def __init__(self, t_name):  
        threading.Thread.__init__(self, name=t_name)  
    def run(self):  
        global x  
        con.acquire()  
        if x > 0:  
            con.wait()  #等待
        else:  
            for i in range(5):  
                x=x+1  
                print("producing..." + str(x))  
            con.notify()   # 唤醒
        print(x)  
        con.release()  
  
class Consumer(threading.Thread):  
    def __init__(self, t_name):  
        threading.Thread.__init__(self, name=t_name)  
    def run(self):  
        global x  
        con.acquire()  
        if x == 0:  
            print('consumer wait1')  
            con.wait()  
        else:  
            for i in range(5):  
                x=x-1  
                print("consuming..." + str(x))  
            con.notify()  
        print(x)  
        con.release()  
con = threading.Condition()   
x=0   
print('start consumer')   
c=Consumer('consumer')   
print('start producer')  
p=Producer('producer')     
p.start()   
c.start()   
p.join()  
c.join()   
print('last',x)  
##在初始状态下，Consumer处于wait状态，Producer连续生产（对x执行增1操作）5次后，notify正在等待的Consumer。Consumer被唤醒开始消费（对x执行减1操作） 
