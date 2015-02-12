import pysock
ip = '192.168.1.103'
port = 51423
ser = pysock.new_server()
client = ser.open_UDP()
client.connect((ip,port))
client.sendall('hello')
try:
    print client.recv(1024)
except(IOError):
    print 'lose'
    pass
client.close()
