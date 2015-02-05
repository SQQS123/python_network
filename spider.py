import urllib2,re
url = 'http://www.baidu.com'
req = urllib2.Request(url)
web = urllib2.urlopen(req,data = None,timeout = 3)
r = web.read()
d=[]
c = re.findall(r'<a href="http://.*?" ',r)
for i in c:
    d.append(i)
    d.append('\n')
str1 = ''.join(d)
f = re.findall(r'".*?"',str1)
for i in f:
    print i


