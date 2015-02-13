#-*-coding:cp936-*-
import pysock
host = ''
port = 51423
ser = pysock.new_server()
s = ser.open_UDP()
s.bind((host,port))
while True:
    print '等待连接...'
    try:
        message,address = s.recvfrom(1024)
        print '收到来自%s的连接'%str(address)
        print message
        data = raw_input('请输入回复内容，若为空则退出:')
        if data:
            s.sendto(data,address)
        else:
            break
        print '______________________________________'
    except(IOError):
        print '网络错误'
        pass
        
