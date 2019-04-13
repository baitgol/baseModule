#!/usr/bin/env python
#coding : utf-8

from ctypes import * 

dll = CDLL('test.so')
a = dll.f()
print a


inta = c_int(4)
intb = c_int(3)
print dll.add(3,4)


