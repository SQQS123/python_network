import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#q = b'>:\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07google\x03com\x00\x00\x01\x00\x01'
q = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x05baidu\x03com\x00\x00\x01\x00\x01'
print q
print '----------------------------'
#s.sendto(q,('208.67.222.222',53))
s.sendto(q,('8.8.8.8',53))
c = s.recv(4096)
print c
for i in c:
    t = ord(i)
    #print '%x'%t
    print t
s.close

