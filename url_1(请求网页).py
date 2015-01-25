import sys,urllib
url = sys.argv[1]
web = urllib.openurl(url)
if int(web.getcode()) == 200:
  print web.info()
