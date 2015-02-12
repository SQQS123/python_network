import time,traceback,struct
import pysock
host = ''
port = 51423
ser = pysock.new_server()
s = ser.open_UDP()
s.bind((host,port))
print 'waiting for connection...'

while 1:
    message,address = s.recvfrom(8192)
    secs = int(time.time())
    secs += 2208988800
    reply = struct.pack("!I",secs)
    s.sendto(reply,address)
