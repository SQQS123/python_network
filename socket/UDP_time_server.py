import time,sys
import pysock
host = ''
port = 51423
ser = pysock.new_server()

while True:
    print 'waiting for connection...'
    try:
        s = ser.open_UDP()
        s.bind((host,port))
        message,address = s.recvfrom(8192)
        print "got data from %s"%str(address)
        print message
        secs = int(time.time())
        secs += 2208988800
        s.sendto(str(secs),address)
        s.close()
    except(IOError):
        sys.exit(1)
