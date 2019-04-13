#!/usr/bin/python
# -*- coding: utf-8 -*-

# MySQLdb.py

import MySQLdb

conn=MySQLdb.connect(host='10.45.134.206',user='root',passwd='root',db='test',charset='utf8')
cur=conn.cursor()

sql='show tables'
cur.execute(sql)
#data=cur.fetchone()
#print data,".................."

for row in cur.fetchall():
    for r in row:
	    print r
print " "
cur.close()
conn.close()

