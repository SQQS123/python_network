import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
q = b'>:\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07baidu\x03com\x00\x00\x01\x00\x01'
s.sendto(q,('10.89.64.5',53))
print s.recv(4096)
s.close
raw_input()
