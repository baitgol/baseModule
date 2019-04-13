#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

fp = open('myjson.txt','rb')
obj = fp.read()
print obj
#str->dict
dct = json.loads(obj)
print dct
#ict->str
asjon = json.dumps(dct)
print type(asjon)