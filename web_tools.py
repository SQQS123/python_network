#-*-coding:utf-8-*-
import socket,urllib,urllib2,time
class tools():
    def _init_(self):
        pass
    def test_google(self):
        t1 = time.time()
        tim = 0
        for i in range(122):
            g = i+1
            url = "http://210.242.125.%d" %g
            req = urllib2.Request(url)
            try:
                google = urllib2.urlopen(req,data = None,timeout = 0.5)
                tim = tim+1
                print url + "------------->" +"HTTP 200 OK"
                #print google.info()
            except(IOError):
                pass
        t2 = time.time()
        t = str(t2-t1)
        print "#####################################"
        print "共找到%s条,耗时%ss"%(tim,t)
        print "#####################################"
        
                


        
