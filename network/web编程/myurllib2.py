#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)
#req = urllib2.Request('http://www.example.com/')
#req.add_header('Referer', 'http://www.python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()