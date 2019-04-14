#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib.parse

'''
URL 使用这种格式：
prot_sch://net_loc/path;params?query#frag
--------------------------------------------
Table 20.1 Web Address Components
URL 部件 描述
prot_sch 网络协议或者下载规划
net_loc 服务器位置(或许也有用户信息)
path 斜杠( / )限定文件或者CGI 应用程序的路径。
Params 可选参数
query 连接符( & )连接键值对
frag 拆分文档中的特殊锚
--------------------------------------------
'''

#urlparse 模块处理url
url_parse=urllib.parse.urlparse('http://www.python.org/doc/FAQ.html;abc?123#456')
print(url_parse)
#ParseResult(scheme='http', netloc='www.python.org', path='/doc/FAQ.html', params='abc', query='123', fragment='456')
#urlparse(urlstr, defProtSch=None, allowFrag=None)
'''urlparse()将urlstr 解析成一个6-元组(prot_sch, net_loc,path, params, query,
frag).这里的每个部件在上边已经描述过了。如果urlstr 中没有提供默认的网络协议或下载规划时
可以使用defProtSch。allowFrag 标识一个URL 是否允许使用零部件。下边是一个给定URL 经
urlparse() 后的输出：
'''
url=urllib.parse.urlunparse(url_parse)
print(url)
#将URL数据(urltup)的一个元组反解析成一个URL 字符串。

url_new=urllib.parse.urljoin('http://www.python.org/doc/FAQ.html', 'current/lib/lib.htm')
print(url_new)
#'http://www.python.org/doc/current/lib/lib.htm'
#urljoin()取得baseurl，并将其基路径(net_loc 附加一个完整的路径，但是不包括终端的文件)与newurl 连接起来。例如：