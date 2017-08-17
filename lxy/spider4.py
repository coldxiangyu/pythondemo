# author: coldxiangyu
# encoding=utf-8

import re
import os
import urllib.request

def getContent(url):
    content = urllib.request.urlopen(url).read().decode('utf-8')
    return content

def getPreLink(content):
    pattern = re.compile(r'<title>(.*?)</title>.*?<div class="pre">.*?<p>.*?<a href="(.*?)">(.*?)</a>.*?</p>.*?</div>.*?<div class="nex">',re.S);
    items = re.findall(pattern, content)
    return items[0]

def getImageList(content):
    imagelist = re.findall('img src="(http.*?)"',content)
    return imagelist

def call(url):
    content = getContent(url)
    item = getPreLink(content)
    imagelist = getImageList(content)
    print('《' + item[0] + '》','共有', len(imagelist), '张图片需要保存！')
    saveImage(item, imagelist)
    print('保存完毕：' + url)
    try:
        if item[1] != '':
            new_url = root_url + item[1]
            call(new_url)
    except Exception as e:
        print("打印完毕！");

def saveImage(item, imagelist):
    arrpath = item[1].split('/')
    filepath = arrpath[0] + arrpath[1] + arrpath[2]
    path = 'D:/MyDownload/blog/' + filepath + '/' + item[2] + '/'
    if not os.path.exists(path):
        os.makedirs(path)
    count = 0
    for url in imagelist:
        print(url)
        if(url.find('.') != -1):
            name = url[url.find('.', len(url) - 5):];
            bytes = urllib.request.urlopen(url)
            f = open(path + str(count) + name, 'wb')
            f.write(bytes.read())
            f.flush()
            f.close()
            count += 1


root_url = "http://www.coldxiangyu.com"
url = "http://www.coldxiangyu.com/2017/08/01/docker-intruduction/"
call(url)
