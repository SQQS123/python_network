import urllib,sys
c=urllib.openurl(sys.argv[1]).read()
o = file('url.txt','r+')
o.write(c)
o.close
