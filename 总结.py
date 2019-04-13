#!/usr/bin/env python
# -*- coding:utf-8 -*-
1. 运算
a.在Python中，有这样一句话是非常重要的：对象有类型，变量无类型。
x = 5
b.from __future__ import division
// % 商，余数
print divmod(5,2)  #表示5除以2，返回了商和余数(2,1)
print round(1.234567,2) #四舍五入
c.math 模块

2. 字符串
a.str() repr()
如r"c:\news"，由r开头引起的字符串，就是原始字符串，在里面放任何字符都表示该字符的原始含义。
b.字符串格式化输出（3种，推荐string.format())
c.split、strip
3. 列表
reversed
'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
因为list.reverse()不返回值，所以不能实现对列表的反向迭代，如果要这么做，可以使用reversed函数（内建函数）。
原地修改的都没有返回值，如append、extend、insert、reverse、sort
sorted_score = sorted(score, reverse=True) 倒序
4.元组
如果一个元组中只有一个元素的时候，应该在该元素后面加一个半角的英文逗号。
>>> a = (3)
>>> type(a)
<type 'int'>
>>> b = (3,)
>>> type(b)
<type 'tuple'>
1）Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
2）如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
3）Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
4）Tuples 可以用在字符串格式化中。

5.字典
字典可以原地修改，即它是可变的。
字典中的“键”，必须是不可变的数据类型；“值”可以是任意数据类型。
基本操作：
len(d)，返回字典(d)中的键值对的数量
d[key]，返回字典(d)中的键(key)的值
d[key]=value，将值(value)赋给字典(d)中的键(key)
del d[key]，删除字典(d)的键(key)项（将该键值对删除）
key in d，检查字典(d)中是否含有键为key的项
>>> temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
>>> my = {"name":"qiwsir", "lang":"python"}
>>> temp % my
'<html><head><title>python<title><body><p>My name is qiwsir.</p></body></head></html>'
方法：
赋值：
>>> ad = {"name":"qiwsir", "lang":"python"}
>>> bd = ad
>>> bd
{'lang': 'python', 'name': 'qiwsir'}
>>> id(ad)
3072239652L
>>> id(bd)
3072239652L
copy
>>> cd = ad.copy()
>>> cd
{'lang': 'python', 'name': 'qiwsir'}
>>> id(cd)
3072239788L
但是字典中值有列表情况
>>> x = {"name":"qiwsir", "lang":["python", "java", "c"]}
>>> y = x.copy()
>>> y
{'lang': ['python', 'java', 'c'], 'name': 'qiwsir'}
>>> id(x)
3072241012L
>>> id(y)
3072241284L
>>> y["lang"].remove("c")
>>> y
{'lang': ['python', 'java'], 'name': 'qiwsir'}
>>> x
{'lang': ['python', 'java'], 'name': 'qiwsir'}
>>> id(x["lang"])
3072243276L
>>> id(y["lang"])
3072243276L
deepcopy
get,setdefault
>>> print d.get("name")
None
>>> d["name"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'
这就是dict.get()和dict['key']的区别。
get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
setdefault(...)
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
items/iteritems, keys/iterkeys, values/itervalues
pop, popitem
pop(...)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised
update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
    If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
    In either case, this is followed by: for k in F: D[k] = F[k]
has_key

6.语句
三元操作符A = Y if X else Z
如果X为真，那么就执行A=Y
如果X为假，就执行A=Z
zip
>>> result
[(2, 11), (4, 13), (6, 15), (8, 17)]
>>> zip(*result)
[(2, 4, 6, 8), (11, 13, 15, 17)]
enumerate
list解析
for while if

7.文件
with open("130.txt","a") as f:
8.迭代
score=[random.randint(0,100) for i in range(40)]
9.自省
10.函数
命名：
文件名:全小写,可使用下划线
函数名:小写，可以用下划线风格单词以增加可读性。如：myfunction，my_example_function。注意：混合大小写仅被允许用于这种风格已经占据优势的时候，以便保持向后兼容。有的人，喜欢用这样的命名风格：myFunction，除了第一个单词首字母外，后面的单词首字母大写。这也是可以的，因为在某些语言中就习惯如此。
函数的参数：如果一个函数的参数名称和保留的关键字(所谓保留关键字，就是python语言已经占用的名称，通常被用来做为已经有的函数等的命名了，你如果还用，就不行了。)冲突，通常使用一个后缀下划线好于使用缩写或奇怪的拼写。
变量:变量名全部小写，由下划线连接各个单词。如color = WHITE，this_is_a_variable = 1。
def foo(x,y=2,*targs,**dargs):
几个特殊函数：
filter、map、reduce、lambda、yield

1）lambda arg1, arg2, ...argN : expression using arguments
在lambda后面直接跟变量
变量后面是冒号
冒号后面是表达式，表达式计算结果就是本函数的返回值

2）map(function, iterable, ...)
对iterable中的每个元素，依次应用function的方法（函数）（这本质上就是一个for循环）。
将所有结果返回一个list。
如果参数很多，则对那些参数并行执行function。

3）reduce
map是上下运算，reduce是横着逐个元素进行运算。
>>> reduce(lambda x,y: x+y,[1,2,3,4,5])
15
4）filter
>>> numbers = range(-5,5)
>>> numbers
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
>>> filter(lambda x: x>0, numbers)
[1, 2, 3, 4]

11.类
类和实例
self的作用
继承的特点，即将父类的方法和属性全部承接到子类中；如果子类重写了父类的方法，就使用子类的该方法，父类的被遮盖。
super函数
因为在子类中重写了某个方法之后，父类中同样的方法被遮盖了。那么如何再把父类的该方法调出来使用呢？纵然被遮盖了，应该还是存在的，不要浪费了呀。如__init__()函数
super(Girl, self).__init__()
#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type #新式类

class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print "{} is about {}".format(name, self.height)

class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()
        self.breast = 90

    def about(self, name):
        print "{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast)
        super(Girl, self).about(name)

if __name__ == "__main__":
    cang = Girl()
    cang.about("canglaoshi")

静态方法和类方法
@staticmethod表示下面的方法是静态方法
@classmethod表示下面的方法是类方法
多态和封装
封装和私有化
python中私有化的方法也比较简单，就是在准备私有化的属性（包括方法、数据）名字前面加双下划线
特殊方法

12.迭代器
__iter__()是类中的核心，它返回了迭代器本身。一个实现了__iter__()方法的对象，即意味着其实可迭代的。
含有next()的对象，就是迭代器，并且在这个方法中，在没有元素的时候要发起StopIteration()异常。
#!/usr/bin/env python
# coding=utf-8

"""
the interator as range()
"""
class MyRange(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    x = MyRange(7)
    print "x.next()==>", x.next()
    print "x.next()==>", x.next()
    print "------for loop--------"
    for i in x:
        print i

列表的确非常好，在很多时候效率很高，并且能够解决相当普遍的问题。但是，不要忘记一点，在某些时候，列表可能会给你带来灾难。因为在你使用列表的时候，需要将列表内容一次性都读入到内存中，这样就增加了内存的负担。如果列表太大太大，就有内存溢出的危险了。这时候需要的是迭代对象。比如斐波那契数列

13.生成器
我们把含有yield语句的函数称作生成器，生成器是一种用普通函数语法定义的迭代器
14.上下文管理器
with
15.错误和异常
常见异常：
异常	描述
NameError	尝试访问一个没有申明的变量
ZeroDivisionError	除数为0
SyntaxError	语法错误
IndexError	索引超出序列范围
KeyError	请求一个不存在的字典关键字
IOError	输入输出错误（比如你要读的文件不存在）
AttributeError	尝试访问未知的对象属性
try except else finally
16.库
模块、库、包
模块是程序
PYTHONPATH环境变量


17.集合
set(可变集合)与frozenset(不可变集合)的区别：
set无序排序且不重复，是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交集), difference(差集)和sysmmetric difference(对称差集)等数学运算.
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, 或其它类序列的操作。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。