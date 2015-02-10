import socket,sys
host = ''
port = 51423
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
while True:
    print 'waiting for connection...'
    try:
        message,address = s.recvfrom(8192)
        print "got data from "+str(address)
        print message
        s.sendto(message,address)
    except(IOError):
        print "error"
        sys.exit(1)
