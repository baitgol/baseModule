# -*- coding: UTF-8 -*-
import sys,os
import time
import random
import string
import re

def muti_replace(adict, text):
    rx = re.compile('|'.join(map(re.escape, adict.keys())))
    return rx.sub(lambda m :adict[m.group()], text)

if __name__ =='__main__':
    text = "My name is Kang Liu,I come from Fudan University. BigFudan"
    adict = {"Fudan":"WuJiaoChang",
             "Kang Liu":"Tomsheep"
             }
    print muti_replace(adict,text)

