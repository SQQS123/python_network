#-*-coding:cp936-*-
import pysock
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')
host = raw_input('������ip��ַ')
port = 51423
ser = pysock.new_server()
s = ser.open_UDP()
while True:
    try:
        s.connect((host,port))
        s.sendall('������')
        message,address = s.recvfrom(1024)
        print '�յ�����%s������:'%str(address)
        if message:
            user32.MessageBoxA(0,message,'��Ϣ',0)
        data = raw_input('����������:')
        s.sendto(data,address)
        print '________________________________'
    except(IOError):
        print '�������'
        pass
        
