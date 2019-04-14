#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
# 正则表达式
# 通配符
# . 表示与任何一个字符进行匹配
# * 表示与此前的字符匹配0或者多次
# ? 匹配0 或者1 次   限定符
# + 1次 或 多次
# .* 最大匹配
# .*? 最小匹配
# ^ 开头\A   $结尾 \Z
# \b 单词的边界 \B
# \d  十进制数字  \D
# \w  任何字母数字 \W
# \s  任何空格字符（空格、tab、换行。。。） \S
#方法：
#re.compile(strPattern[, flag]):
"""
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变'.'的行为
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：
"""
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)
#group([group1, …]):
#获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。
# group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；
# 没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
print("m.group(1):", m.group(1))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

m=re.search(r'world','Hello world!')
print('search:', m.group())

p = re.compile(r'\d+')
print('findall:', p.findall('one1two2three3four4'))

p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print(m.group(), end=' ')
print()
p = re.compile(r'\d+')
print('split:', p.split('one1two2three3four4'))

#sub
"""
sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
count用于指定最多替换次数，不指定时全部替换。 
"""
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print('sub:', p.sub(r'\2 \1', s))

def func(m):
    print(m.group(1).title())
    print(m.group(2).title())
    return m.group(1).title() + ' ' + m.group(2).title()
print(p.sub(func, s))

#subn返回 (sub(repl, string[, count]), 替换次数)。

