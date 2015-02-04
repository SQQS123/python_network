import urllib
for i in range(98):
    t = i+1
    o = file('url.txt','w+')
    url = "http://211.242.152.%d"%t
    try:
        google = urllib.urlopen(url)
        cheak = int(google.getcode())
        print url + cheak
        if cheak == 200:
            o.write("#")
            o.write(url)
            o.write("@")
    except(IOError):
        print 'this url(%s)is not work'%url
        pass
o.close()
    
