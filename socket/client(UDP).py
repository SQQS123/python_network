import pysock
ip = '192.168.1.103'
port = 51423
ser = pysock.new_server()
client = ser.open_UDP()
client.connect((ip,port))
while True:
    code = raw_input('>:')
    client.sendall(code)
    try:
        print client.recv(1024)
    except(IOError):
        print 'lose'
        pass

