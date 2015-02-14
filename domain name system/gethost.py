import sys,socket
result = socket.gethostbyaddr('192.30.252.128')
print result[0]
