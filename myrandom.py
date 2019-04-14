# -*- coding: cp936 -*-
import random


#random

print((random.uniform(10,20)))
print((random.uniform(20,10)))
print((random.randint(10,20)))
print((random.randrange(10,100,2)))
#=
print((random.choice(list(range(10,100,2)))))

print((random.choice("abcdefg")))
print((random.choice(['a','b','c'])))
print((random.choice(('a','b','c'))))

p = ['python','is','powerful','simple','and so on....']
random.shuffle(p)  #打乱排序
print(p)

print((random.sample('abcdefg',3)))


