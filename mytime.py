#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from datetime import datetime

"""
表示日常所用时间的类，是用C实现的内嵌类。
功能比较简单，但效率高。表示的时间范围有限1970年1月1日到2038年1月19日。
"""

"""
当前时间 
返回的一个float型，以一个固定时间epoch(1970年1月1日0时起经过的秒数)
因为time终究是以float型来表示的，所以对于timespan的问题，基本就成了数字问题。
"""
"""
a.时间戳(timestamp)：从1970年1月1日00:00:00到现在为止一共的时间数（单位为秒）
b. 格式化的时间字符串(format string)
c. struct_time(元组)
"""
#timestamp
print(time.time())
# str
print(time.ctime())

#struct_time
print(time.localtime())
"""
使用localtime 返回一个time结构，
其中包括tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst=0 夏令时间标志
tm_wday为周几，0是周一，6是周日
"""
#这个返回UTC时间
print(time.gmtime())

#转换

#1.
#timstamp -> struct_time
time_struct = time.localtime(time.time())

#time.struct_time(tm_year=2014, tm_mon=12, tm_mday=1, tm_hour=11, tm_min=5, tm_sec=25, tm_wday=0, tm_yday=335, tm_isdst=0)
#struct_time -> timestamp
time.mktime(time_struct)

#2.
#struct_time -> str
time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
#str-> struct_time
time.strptime('2014-12-01 11:14:02', "%Y-%m-%d %H:%M:%S")


#3.
# timestamp -> str
time.ctime(time.time())
tm = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(currenttime))
#str -> timestamp （str->strct->timestamp)
time.mktime(time.strptime('2014-12-01 11:14:02', "%Y-%m-%d %H:%M:%S"))


past = (2010, 11, 12, 13, 14, 15 , 0 , 0 , 0)
print time.asctime(past)
print time.localtime(time.mktime(past))

currenttime = int(time.time())
tm = time.strftime("%Y%m%d%H%M%S",time.localtime(currenttime))
print tm

now = datetime.now()
