#-*-coding:cp936-*-
import socket
list1 = []
list2 = []
list3 = []
list4 = []
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x = 17
#x=15
#q = b'>:\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x08facebook\x03com\x00\x00\x01\x00\x01'
q = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'
print '----------------------------'
#s.sendto(q,('208.67.222.222',53))
s.sendto(q,('8.8.8.8',53))
c = s.recv(4096)
print 'DNS������ϢΪ��'
print '��ʶΪ��%x%x'%(ord(c[0]),ord(c[1]))
print '��־Ϊ��%x%x'%(ord(c[2]),ord(c[3]))
print '��������%x%x'%(ord(c[4]),ord(c[5]))
print 'Ӧ������%x%x'%(ord(c[6]),ord(c[7]))
print '��Ȩ������%x%x'%(ord(c[8]),ord(c[9]))
print '������Ϣ����%x%x'%(ord(c[10]),ord(c[11]))
for i in range(x):
    num=i+11
    list1.append(str(ord(c[num])))
str1 = ' '.join(list1)
print "��ѯ����%s"%str1
x2 = int(list1[1])
for i in range(x2):
    x3 = int(list1[i+2])
    x4 = chr(x3)
    list2.append(x4)
str2 = ''.join(list2)
#print str2
x5 = int(list1[x2+2])
for i in range(x5):
    x6 = int(list1[x2+3+i])
    x7 = chr(x6)
    list3.append(x7)
str3 = ''.join(list3)
#print str3
judg = x5+x2+4
if judg == len(list1):
    print '��ѯ��ϢΪ:%s.%s'%(str2,str3)
else:
    x8 = int(list1[x5+x2+3])
    for i in range(x8):
        x9 = int(list1[x5+x2+4+i])
        x10 = chr(x9)
        list4.append(x10)
    str4 = ''.join(list4)
    #print str4
    judge = x2+x5+x8+5
    if judge == len(list1):
        print '��ѯ��ϢΪ:%s.%s.%s'%(str2,str3,str4)
    else:
        print '���󣺱�����֧�ֳ�������������������'
print '��ѯ����:%x%x'%(ord(c[x+11]),ord(c[x+12]))
print '��ѯ�ࣺ%x%x'%(ord(c[x+13]),ord(c[x+14]))
print 'ָ�룺%x%x'%(ord(c[x+15]),ord(c[x+16]))
print '��һ����Դ����Ӧ���ͣ�%x%x'%(ord(c[x+17]),ord(c[x+18]))
print '��һ����Դ����Ӧ�ࣺ%x%x'%(ord(c[x+19]),ord(c[x+20]))
print '��һ����Դ������ʱ�䣺%x%x%x%x'%(ord(c[x+21]),ord(c[x+22]),ord(c[x+23]),ord(c[x+24]))
print '��һ����Դ�����ݳ��ȣ�%x%x'%(ord(c[x+25]),ord(c[x+26]))
print '���ص�IP��ַ��%d.%d.%d.%d'%(ord(c[x+27]),ord(c[x+28]),ord(c[x+29]),ord(c[x+30]))
if len(c) == x+31:
    print '�������'
else:
    print 'DNS����ֹһ����Ϣ�����������������Ϣ������'


