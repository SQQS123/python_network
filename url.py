import urllib,sys
c=urllib.openurl(sys.argv[1])
d=c.read()
o = file('url.txt','r+')
o.write(d)
o.close
