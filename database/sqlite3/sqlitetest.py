#!/usr/bin/env python
#conding: utf-8

import sqlite3

conn = sqlite3.connect('test.db')
cu = conn.cursor()
create_table_sql = 'create table task( id integer primary key ,pid integer , name varchar(10))'
cu.execute(create_table_sql)
insert_sql = "insert into task values(0,0,'task1')"
cu.execute(insert_sql)
cu.execute('insert into task values(1,1,"task2")')

cu.execute("select * from task")
print 'after insert',cu.fetchall()
#update
cu.execute("update task set name = 'task_2' where id = 1")

cu.execute("select * from task")

print 'after update',cu.fetchall()

conn.commit()
cu.execute("select * from task")
print 'after delete',cu.fetchall()

cu.close()
conn.close()
