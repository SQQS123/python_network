#-*-coding:cp936-*-
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
        raw_input("请按任意键退出")

    def scan_all_port(self,ip):
        t1 = time.time()
        tim = 0
        dl =[]
        for i in range(80):
            port = i+1
            sock = socket.socket()
            socket.setdefaulttimeout(0.5)
            port_s = str(port)
            print "尝试打开%s的%s端口"%(ip,port_s)
            try:
                sock.connect((ip,port))
                print "该端口打开"
                dl.append(port_s)
                tim = tim+1
            except(IOError):
                print "该端口未打开"
                pass
        t2 = time.time()
        t = str(t2-t1)
        print "#####################################"
        print "共找到%s条,耗时%ss"%(tim,t)
        print "#####################################"
        for i in dl:
            print ip+':'+i
        raw_input("请按任意键退出")
            

            
                
        
        
        
        
        
                


        

                


        
