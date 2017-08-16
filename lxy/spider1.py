#coding = utf-8
import urllib.request,os

#page = urllib.request.urlopen('http://www.coldxiangyu.com/2017/08/01/docker-intruduction/').read()
req_url_root = 'http://www.coldxiangyu.com/2017/08/01/docker-intruduction/'
req_header = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'Hm_lvt_cf8506e0ef223e57ff6239944e5d46a4=1500618036,1500943985,1500971967,1501052247; _gat=1; _ga=GA1.2.20094576.1498790339; _gid=GA1.2.1124598432.1501817058',
'Host':'www.coldxiangyu.com',
'If-Modified-Since':'Wed, 02 Aug 2017 01:24:43 GMT',
'Referer':'http://www.coldxiangyu.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3107.4 Safari/537.36'
}


bytes = urllib.request.urlopen(req_url_root)
content = bytes.read()
if not os.path.exists("/home/coldxiangyu/MyDownload"):
    os.mkdir("/home/coldxiangyu/MyDownload")
f = open("/home/coldxiangyu/MyDownload/content.txt", 'w')
content = content.decode('utf-8')
f.write(content)
f.close()
print(content)


