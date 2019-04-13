#coding:utf-8

from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.ini')

section = config.sections()
print 'section:',section

option = config.options('mail')  
print 'mail:',option

kvs = config.items('mail')  #键值对
print 'mail:', kvs  

print config.get('mail','Field_NUM')

config.set('mail','Field_NUM','0')

print config.get('mail','Field_NUM')


#config.add_section('im')
#config.set('im','table','trs_im')

config.write(open('config.ini','w'))  #写入文件

