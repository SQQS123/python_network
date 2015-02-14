import sys,socket
result = socket.getaddrinfo('www.baidu.com',None)
for i in result:
    print 'socketaddr:%s'%str(i[4][0])

