# from datetime import datetime
# # datetime
# now=datetime.now()
# print(now)
# dt=datetime(2015,4,19,12,20)
# print(dt)
# # 转化为日期时间格式
# print(dt.timestamp())


# #nametuple类型，可以直接给属性赋值
# from collections import namedtuple
# Point=namedtuple('Point',['x','y'])
# p=Point(1,2)
# print('p.x=%s'% p.x)
# print('p.y=%s'%p.y)


# # 队列
# from collections import deque
# q=deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)


# # counter计数，统计
# from collections import Counter
# c=Counter()
# for ch in 'programming':
#     c[ch]=c[ch]+1
# print(c)


# # hashlib哈希算法
# import hashlib
# md5=hashlib.md5()
# md5.update('how to do it'.encode('utf-8'))
# print(md5.hexdigest())


# # itertools 迭代
# import itertools
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))

# #xml处理
# from xml.parsers.expat import ParserCreate
# class DefaultSaxHandler(object):
#     def start_element(self,name,attrs):
#         print('sax:start_element:%s,attrs:%s' %(name,str(attrs)))
#     def end_element(self,name):
#         print('sax:end_element:%s'% name)
#     def char_data(self,text):
#         print('sax:char_data:%s'%text)


# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)    


# # html处理
# from html.parser import HTMLParser
# from html.entities import name2codepoint
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self,tag,attrs):
#         print('<%s>' % tag)
#     def handle_endtag(self,tag):
#         print('%s' % tag)
#     def handle_startendtag(self,tag,attrs):
#         print('%s' % tag)
#     def handle_data(delg,data):
#         print(data)
#     def handle_comment(self,data):
#         print('<!--',data,'-->')
#     def handle_entityref(self,name):
#         print('&%s' % name)
#     def handle_charref(self,name):
#         print('&#%s:' % name)
# parser=MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')  
    
# request请求url 
from urllib import request
with request.urlopen('http://www.python.org/events/python-events/') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('Data',data.decode('utf-8'))
