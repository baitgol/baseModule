#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 表trs_stat_mobiconn直接插入数据
# 要求：
# 号码信息来自PhoneInfo.txt，最多不超过1000万
# 时间跨度1个月，当前时间向前推1个月
# 数据量每天1亿
# 两个子库均衡分布
# 某些特定号码（查询目标号码）每天至少与个不同10的其他号码联系，能够验证查询结果的正确性
# 表rls_mobiconn直接插入数据
# 要求：
# 号码信息来自PhoneInfo.txt，最多不超过1000万
# 时间跨度1个月，当前时间向前推1个月
# 数据量每天500万，可增至2000万
# 两个子库均衡分布
# 某些特定号码（查询目标号码），查询结果能够展示5层关系（超出300节点后，页面提示，需要手动扩展），能够验证查询结果的正确性。
# tanglei  2014-12
import os
import time
import random
import cx_Oracle

# 读号码
fp = open('PhoneInfo_10000000.txt', 'r')
list1 = fp.readlines()
ph_count = len(list1)
msisdn_list = [list1[i].split('\t')[0] for i in range(ph_count)]
fp.close()
#
# special_num =msisdn_list[0:10] #特定号码
# 数据库连接
ora = 'pfdb/pfdb@162.168.2.73/ora11g'  # 需要根据数据库修改
conn = cx_Oracle.connect(ora)


# 时间转换：当前时间->当天0点时间的时间戳形式
def mk_start_time(a):
    b = (a.tm_year, a.tm_mon, a.tm_mday, 0, 0, 0, a.tm_wday, a.tm_yday, a.tm_isdst)
    return int(time.mktime(b))


sourceno = ['DST_015002', 'DST_015003']
prototype = ['7', '6']
today_starttime = mk_start_time(time.localtime())
starttime = 1419350400  # 24号 #mk_start_time(time.localtime())  #一天的开始时间
endtime = starttime + 86399  # 一天的结束时间
one_day_second = 86400


# 函数insert_trs_all_by_dual：插入trs_stat_mobiconn表数据
# count表示每天多少数据量
# 通过oralce虚表dual来多行插入数据，往单个oracle库插入数据

def insert_trs_all_by_dual(count, i):
    # 插入30天的数据
    start = time.time()
    start_time = starttime - i * one_day_second  # 一天的开始时间
    end_time = endtime - i * one_day_second  # 一天的结束时间
    if today_starttime == starttime:
        end_time = int(time.time())  # 当天数据
    print "#######insert data to trs capturetime between %s and %s######" % (start_time, end_time)
    sql = "insert into trs_stat_mobiconn "
    select_sql = ""
    for j in range(45641900, count):  # 每天的数据量
        # 字段定义
        capturetime = random.randint(start_time, end_time)
        # h = random.randint(0,1)
        source_no = sourceno[j % 2]  # 确保同号码情况下协议一样010101...
        proto_type = prototype[j % 2]  # 确保同号码情况下协议一样
        tid = str(capturetime) + '14021' + str(random.randint(1000, 9999))
        # uuid = random.randint(0,1)
        uuid = 1  # 73 1 ； 75 0   需要根据数据库修改
        # sender =msisdn_list[random.randint(0,10000000-1)]
        # receiver = msisdn_list[random.randint(0,10000000-1)]
        # 号码循环发送
        s_index = j % ph_count
        r_index = (j + 1) % ph_count
        sender = msisdn_list[s_index]
        receiver = msisdn_list[r_index]
        # print "sender : %s  ; receiver : %s  ; source_no: %s ; proto_type : %s "%(sender,receiver,source_no,proto_type)
        # 字段定义
        num = 100  # num条执行一次插入操作
        select_sql = select_sql + "select '%s','%s','%s',%d,'%s',%d,'%s' from dual union " % (
        sender, receiver, proto_type, capturetime, source_no, uuid, tid)
        if (j + 1) % num == 0:  # j=num-1 num条执行一次插入
            cur = conn.cursor()
            insert_sql = sql + select_sql
            insert_sql = insert_sql[:-6]  # 去掉字符串末尾的'union '
            cur.execute(insert_sql)
            conn.commit()
            cur.close()
            select_sql = ""  # 注意 字符串重置
    end = time.time()
    run_time = end - start
    print 'run time : %s' % run_time


def insert_rls_all_by_dual(count, i):
    start = time.time()
    start_time = starttime - i * one_day_second  # 一天的开始时间
    print "#####insert data to rls capturetime = %s#####" % (start_time)
    sql = "insert into rls_mobiconn "
    select_sql = ""
    for j in range(count):
        # 字段定义
        capturetime = start_time  # 每天的00:00:00
        # h = random.randint(0,1)
        source_no = sourceno[j % 2]  # 同trs_stat表
        proto_type = prototype[j % 2]  # 同trs_stat表
        cnt = 5  # random.randint(1,4)
        # 号码循环发送
        s_index = j % ph_count
        r_index = (j + 1) % ph_count
        sender = msisdn_list[s_index]
        receiver = msisdn_list[r_index]
        # print "sender : %s  ; receiver : %s  ; source_no: %s ; proto_type : %s "%(sender,receiver,source_no,proto_type)
        # 字段定义
        select_sql = select_sql + "select '%s','%s','%s',%d,%d,'%s' from dual union " % (
        sender, receiver, proto_type, capturetime, cnt, source_no)
        num = 100
        if (j + 1) % num == 0:  # j=num-1 num条执行一次插入
            cur = conn.cursor()
            insert_sql = sql + select_sql
            insert_sql = insert_sql[:-6]  # 去掉字符串末尾的'union '
            cur.execute(insert_sql)
            conn.commit()
            cur.close()
            select_sql = ""  # 注意
    end = time.time()
    run_time = end - start
    print 'run time : %s' % run_time


if __name__ == '__main__':
    print "%s" % time.ctime()
    for i in range(1):
        insert_trs_all_by_dual(50000000, i)
        # insert_rls_all_by_dual(100000000,i)
    conn.close()
