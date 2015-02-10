import socket
host = ''
port = 51423
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((host,port))
print 'waiting for connection...'
sock.listen(3)
while True:
    try:
        clientsock,clientaddr = sock.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    try:
        print clientsock.getpeername()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
