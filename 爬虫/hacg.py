#-*-coding:utf-8-*-
import urllib,urllib2,re
url = 'http://www.hacg.in/wordpress/54407'
req = urllib2.Request(url)
web = urllib2.urlopen(req)
str1 = web.read()
#print str1

print url
list1 = re.findall(r'<title>.*?e',str1)
str2 = ''.join(list1)
print str2
list2 = re.findall(u"本站不提供下载\w+",str1.decode('utf8'))

if list2:
    for i in list2:
        #print "\t",i
        final =  re.findall(r'\w+',i)
        str4 = ''.join(final)
        link = 'magnet:?xt=urn:btih:%s'%str4.decode('ascii')
        print link
else:
    list3 = re.findall(u"本站不提供下载 \w+",str1.decode('utf8'))
    for i in list3:
        final = re.findall(r'\w+',i)
        str4 = ''.join(final)
        link = 'magnet:?xt=urn:btih:%s'%str4.decode('ascii')
        print link
