import urllib
from PIL import Image


for i in range(1):
    
    c=urllib.urlopen('http://211.70.49.127/CheckCode.aspx')
    d=c.read()
    cs=i+1
    o = file('cheak%d.png'%cs,'wb')
    o.write(d)
    o.flush()
    o.close
    print "��%d���߳��ѳɹ�ץȡ��֤��..."%cs
    
im = Image.open('cheak1.png')
im.show()
