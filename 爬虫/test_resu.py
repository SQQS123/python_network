#-*-coding:utf-8-*-
import re,urllib2
url = 'http://www.hacg.in/wordpress'
req = urllib2.Request(url)
web = urllib2.urlopen(req)
str1 = web.read()
#print str1
list1 = re.findall(r'http://www.hacg.in/wordpress/\d+',str1)
list2 = list(set(list1))
for i in list2:
    print url

    

