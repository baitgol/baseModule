#coding: cp936
#�����ض��ļ����������ı��ļ����ض���׺�������ض��ַ�
import os

def Search(rootdir,suffixes,arg):
    for lists in os.listdir(rootdir):
        path = os.path.join(rootdir,lists)
        if os.path.isfile(path):   #file
            if path.endswith(suffixes):
                try:
                    with open(path,encoding='utf-8') as fh:
                        lineNum = 0
                        for line in fh:
                            lineNum += 1
                            if arg in line:
                                print(lineNum, ':',path)
                                print(line)
                except:
                    print('error:',path)
        if os.path.isdir(path):
            Search(path,suffixes,arg)

Search(r'D:\��Ŀ\python\test\base module',('.c','.cpp','.py'),'cx_Oracle')
##            
            
