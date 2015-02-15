#-*-coding:cp936-*-
import pysock
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')
host = raw_input('请输入ip地址')
port = 51423
ser = pysock.new_server()
s = ser.open_UDP()
while True:
    try:
        s.connect((host,port))
        s.sendall('已连接')
        message,address = s.recvfrom(1024)
        print '收到来自%s的内容:'%str(address)
        if message:
            user32.MessageBoxA(0,message,'消息',0)
        data = raw_input('请输入内容:')
        s.sendto(data,address)
        print '________________________________'
    except(IOError):
        print '网络错误'
        pass
        
