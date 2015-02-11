#-*-coding:utf-8-*-
import urllib,urllib2,re
url = 'http://www.hacg.in/wordpress/54502'
req = urllib2.Request(url)
web = urllib2.urlopen(req)
str1 = web.read()
#print str1
print url
str2 = re.findall(r'<title>.*?</title>',str1)
for i in str2:
    print "\t",i
ccc = re.findall(u"本站不提供下载\w+",str1.decode('utf8'))
for i in ccc:
   #print "\t",i
   final =  re.findall(r'\w+',i)
   str4 = ''.join(final)
   lj = 'magnet:?xt=urn:btih:%s'%str4.decode('ascii')
   print lj
