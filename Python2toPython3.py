#coding:utf-8
import os

def Python2toPython3(dirname, p2to3FileName):
    if os.path.exists(dirname):
        for dirpath, dirnames, filenames in os.walk(dirname):
            for filename in filenames:
                if filename.endswith('.py'):
                    fileFullName = os.path.join(dirpath, filename)
                    print('Processing File:', fileFullName)
                    pycode2to3 = ("python " + p2to3FileName + " -w " +
                                  fileFullName)
                    try:
                        print((os.popen(pycode2to3, 'r').read()))
                    except:
                        continue




if __name__ == "__main__":
    p2to3FileName = (r'"D:\Program Files (x86)\Anaconda3\Scripts\2to3-script.py"')
    dirname = r"D:\pythonProject\pythonLearning\baseModule\mythread"
    Python2toPython3(dirname, p2to3FileName)