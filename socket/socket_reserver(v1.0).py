import socket
host = ''
port = 51423
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((host,port))
print 'waiting for connection...'
sock.listen(3)
while True:
    clientsock,clientaddr = sock.accept()
    print clientsock.getpeername()
    clientsock.close()

