import urllib,sys
param = urllib.urlencode({'name':'hhh','age':15})
#get方法
web = urllib.openurl("http://192.168.1.101:8080/index.jsp?%s" %param)
#post方法
web = urllib.openurl("http://192.168.1.101:8080/index.jsp",param)
if int(web.getcode()) == 200:
  print web.read()
