import socket
ip = '192.168.1.103'
port = 51423
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect((ip,port))
client.sendall('hello')
client.close()
