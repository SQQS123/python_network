import sys,urllib
url = sys.argv[1]
#filename = urllib.urlretrieve(url)
#若不指定filename则生成临时文件
filename = urllib.urlretrieveu(url,"get.html")
#若指定filename则生成本地文件

