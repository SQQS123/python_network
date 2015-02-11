#-*-coding:utf-8-*-
import urllib2,re,sys
class get_link():
    def _init_(self):
        pass
    def link(self,url):
        req = urllib2.Request(url)
        print 'try to open %s...'%url
        try:
            web = urllib2.urlopen(req)
            str1 = web.read()
        except(IOError):
            print "can not open this url"
            sys.exit(1)
        list1 = re.findall(r'<title>.*?e',str1)
        str2 = ''.join(list1)
        print str2
        
        list2 = re.findall(u"本站不提供下载\w+",str1.decode('utf8'))
        if list2:
            for i in list2:
                final = re.findall(r'\w+',i)
                str4 = ''.join(final)
                link = 'magnet:?xt=urn:btih:%s'%str4.decode('ascii')
                print link
        else:
            list3 = re.findall(u"本站不提供下载 \w+",str1.decode('utf8'))
            if list3:
                final = re.findall(r'\w+',i)
                str4 = ''.join(final)
                link = 'magnet:?xt=urn:btih:%s'%str4.decode('ascii')
                print link
            else:
                print '无资源'
                sys.exit(1)
                



        
            
            
        
    
