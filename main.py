#!/usr/bin/python
#encoding:utf-8
import urllib
import os
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
print "有条件的话请把梯子架上 :-D"
series=raw_input("请输入插件序列：  ")
print series
url = 'https://clients2.google.com/service/update2/crx?response=redirect&x=id%3D'+series+'%26uc'
print url
filename=raw_input("请输入文件名，不用加后缀：  ")
if filename=='':
    filename = url.split('/')[-1]
else:
    filename=filename+'.crx'
filename = unicode(filename , "utf8")
mypath='G:\\下载'
mypath = unicode(mypath , "utf8")
local = os.path.join(mypath,filename)
print local
urllib.urlretrieve(url,local,Schedule)
