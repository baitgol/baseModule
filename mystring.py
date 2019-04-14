#!/usr/bin/env python
# -*- coding:utf-8 -*-
import string
#text
text = 'the cat sat on the mat'
loc = string.index(text,'cat')
#loc = text.index('cat')
print(loc)
last = text.rindex('on') #字符串顺序不变，只是从后开始查找
print(last)

#分离  默认空格 返回列表
print(string.split(text))
#正则表达式
#re.split

#连接 join
#names = string.join(['martin','sharon','wendy'], ',')
names = ','.join(['martin','sharon','wendy'])
print(names)

#截断 默认空格
text = ' the cat sat on the mat '
print(text.lstrip())
print(text.rstrip())
print(text.strip())
text = 'the cat sat on the mat'
#改变大小写
print(text.upper())
#lower()
#capitalize 第一个字符大写
print(text.capitalize())
#capwords 每个单词第一个大写
print(string.capwords(text)) #str 没有capwords函数
#转换
#string.tranlate(text,maketrans('',''))

print(string.replace(text,'cat','dog'))#替换
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.letters)
print(string.lowercase)
print(string.uppercase)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
