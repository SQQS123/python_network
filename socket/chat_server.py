#-*-coding:cp936-*-
import pysock
host = ''
port = 51423
ser = pysock.new_server()
s = ser.open_UDP()
s.bind((host,port))
while True:
    print '�ȴ�����...'
    try:
        message,address = s.recvfrom(1024)
        print '�յ�����%s������'%str(address)
        print message
        data = raw_input('������ظ����ݣ���Ϊ�����˳�:')
        if data:
            s.sendto(data,address)
        else:
            break
        print '______________________________________'
    except(IOError):
        print '�������'
        pass
        
