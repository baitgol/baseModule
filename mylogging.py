# -*- coding: utf-8 -*-
import logging


#默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
#日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别

#将日志输出到文件

# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='a') #'w'

#日志输出到文件
logger = logging.getLogger()
filehandler = logging.FileHandler('myapp.log', mode='w')
formathandler = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
filehandler.setFormatter(formathandler)
logger.addHandler(filehandler)

# logger.setLevel(logging.DEBUG)

#输出到屏幕
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
# logger = logging.getLogger()
console = logging.StreamHandler()
# formathandler = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formathandler)
logger.addHandler(console)
logger.setLevel(logging.INFO)


logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

#logging.basicConfig函数各参数:
#filename: 指定日志文件名
#filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
#format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息
#datefmt: 指定时间格式，同time.strftime()
#level: 设置日志级别，默认为logging.WARNING
#stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

#https://www.cnblogs.com/nancyzhu/p/8551506.html
#
# import logging
# from logging import handlers
#
# class Logger(object):
#     level_relations = {
#         'debug':logging.DEBUG,
#         'info':logging.INFO,
#         'warning':logging.WARNING,
#         'error':logging.ERROR,
#         'crit':logging.CRITICAL
#     }#日志级别关系映射
#
#     def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
#         self.logger = logging.getLogger(filename)
#         format_str = logging.Formatter(fmt)#设置日志格式
#         self.logger.setLevel(self.level_relations.get(level))#设置日志级别
#         sh = logging.StreamHandler()#往屏幕上输出
#         sh.setFormatter(format_str) #设置屏幕上显示的格式
#         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
#         #实例化TimedRotatingFileHandler
#         #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
#         # S 秒
#         # M 分
#         # H 小时、
#         # D 天、
#         # W 每星期（interval==0时代表星期一）
#         # midnight 每天凌晨
#         th.setFormatter(format_str)#设置文件里写入的格式
#         self.logger.addHandler(sh) #把对象加到logger里
#         self.logger.addHandler(th)
# if __name__ == '__main__':
#     log = Logger('all.log',level='debug')
#     log.logger.debug('debug')
#     log.logger.info('info')
#     log.logger.warning('警告')
#     log.logger.error('报错')
#     log.logger.critical('严重')
#     Logger('error.log', level='error').logger.error('error')