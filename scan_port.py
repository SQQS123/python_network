import socket,sys
ip = '192.168.1.103'
ports = [21,22,53,80,443,445,3389,8080]
socket.setdefaulttimeout(2)
for i in ports:
    port = i
    sock = socket.socket()
    print "try to open<%s>:%s"%(ip,port)
    try:
        sock.connect((ip,port))
        print "|___[+]"+ip+":"+str(port)+"   is open"
        sock.close()
    except(IOError):
        pass
