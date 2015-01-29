#!-*-coding:utf-8-*-
import urllib
import urllib2
posturl = 'http://localhost:8080/hhh/login.jsp'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
           'Referer':'http://localhost:8080/hhh/'}
postData = {'username':'sherlock',
            'password':'1234567'}
postData = urllib.urlencode(postData)
request = urllib2.Request(posturl,postData,headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text
