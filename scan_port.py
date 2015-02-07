#-*-coding:cp936-*-
import socket,sys,time
t1 = time.time()
ip = '192.168.1.103'
#ports = [21,22,53,80,443,445,3389,8080]
socket.setdefaulttimeout(0.3)
c=[]
d=0
for i in range(1024):
    port = i+1
    sock = socket.socket()
    print "尝试打开<%s>:%s"%(ip,port)
    try:
        sock.connect((ip,port))
        res = ip+":"+str(port)
        print "|___[+]"+res+" 已打开"
        c.append(res)
        d=d+1
        sock.close()
    except(IOError):
        pass
t2 = time.time()
t = str(t2-t1)
print "*****************************************"
print "##################结果##################"
print "共找到%s个打开的端口,耗时%ss"%(d,t)
print "*****************************************"
for i in c:
    print i
    print "*****************************************"
