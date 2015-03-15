#-*-coding:utf8-*-
import urllib,urllib2,cookielib,re
from PIL import Image
def get_view_code():
    url = 'http://211.70.49.127/'
    req = urllib2.Request(url)
    web = urllib2.urlopen(req)
    text = web.read()
    view = re.findall(r'<input type="hidden" name="__VIEWSTATE" value=".*?" />',text)
    view = str(view)
    value = view.split('"')
    print cj
    print value[5]
    return value[5]
def get():
        web = urllib.urlopen('http://211.70.49.127/CheckCode.aspx')
        pic = web.read()
        name = '1.png'
        fil = file(name,'wb')
        fil.write(pic)
        fil.flush()
        fil.close
        print '验证码获取成功'
        return name
header = {
    'Host':'211.70.49.127',
    'Connection':'keep-alive',
    #'Content-Length':'176',
    'Cache-Control':'max-age=0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin':'http://211.70.49.127',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded',
    #'Referer':'http://211.70.49.127/(aaz2gd45mq34twr3jagvzwau)/default2.aspx',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.8'}
rbl = u'学生'
rbl_e = rbl.encode('gb2312')
data = {
        '__VIEWSTATE':'dDwtMTg3MTM5OTI5MTs7Pl1cb48v/FiKd6cVwa1sp0Euw09l',
        'TextBox1':'1333130026',
        'TextBox2':'340304199502240057',
        'TextBox3':'',
        'RadioButtonList1':'%s'%rbl_e,
        'Button':'',
        'IbLanguage':'',
        }
if __name__ == "__main__":
    cj = cookielib.CookieJar()
    cs = urllib2.HTTPCookieProcessor(cj)
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(cs,httpHandler)
    urllib2.install_opener(opener)
    value = get_view_code()
    get()
    im = Image.open('1.png')
    im.show()
    yzm = int(raw_input(u'请输入验证码'))
    print yzm
    for index, cookie in enumerate(cj):
       print '[',index, ']';
       print cookie.name;
       print cookie.value;
       print "###########################"
  
    

