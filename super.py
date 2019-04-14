#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Base(object):
    def __init__(self):
        print('Base create')
class childA(Base):
    def __init__(self):
        print('enter A ')
        Base.__init__(self)
        #super(childA, self).__init__()
        print('leave A')
class childB(Base):
    def __init__(self):
        print('enter B ')
        # Base.__init__(self)
        super(childB, self).__init__()
        print('leave B')
class childC(childA, childB):
    pass
c = childC()
print(c.__class__.__mro__)
#在多重继承时会涉及继承顺序，super（）相当于返回继承顺序的下一个类，而不是父类