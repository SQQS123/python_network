import urllib2
for i in range(99):
    t = i+1
    url = "http://210.242.125.%d"%t
    req = urllib2.Request(url)
    try:
        google = urllib2.urlopen(req,data = None,timeout=1)
        cheak = int(google.getcode())
        if cheak == 200:
            o = file('url.txt','a')
            o.write("<")
            o.write(url)
            o.write(">")
            o.flush()
            o.close()
            print '<%s> work!'%url
    except(IOError):
        #print "[%s] is not work"%url
        pass
