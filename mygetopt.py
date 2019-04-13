#coding:utf-8

import getopt
import sys

# getopt处理命令行函数
#getopt.getopt(args,shortopts,longopts=[])
# shortopts  短格式（-）; h后面没带冒号表示不带参数；p和i后面带冒号表示带参数
# longopts   长格式(--);带 = 表示后面带参数


try:
    opts,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])
except getopt.GetoptError:
    sys.exit()

for name,value in opts:
    if name in ("-h","--help"):
        print "useage"
    if name in ("-i","--ip"):
        print 'ip is -----',value
    if name in ("-p","--port"):
        print "port is ------",value



