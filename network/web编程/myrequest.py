#coding:utf-8

import requests

data = {'token':'93C4CB5CBDEE19AACBE4FEA9A8DF11B047a0307a3bee44138e930ab70b0ffa47'}
r = requests.get("http://162.168.2.76:8080/portal",params=data)
print(r.status_code)
print(r.url)
print(r.encoding)
#print r.text
#print r.content
#print r.json()
#参数
#allow_redicts = False禁止跳转
#timeout =
# proxies = { "http":"http://10.10.1.10:3128","https" :"https://10.10.1.10:1080",}
#带密码的代理  "http":"http://user:pass@10.10.1.10:3128"
#proxies =  代理
#headers =
print(r.headers['content-encoding'])
print(r.request.headers)