# encoding=utf-8
import urllib.request
import os
import re

def saveimag(iamgelist):
    path = '/home/coldxiangyu/MyDownload/blog/'
    if os.path.exists(path) == False:
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
    url = "http://www.coldxiangyu.com/2017/08/01/docker-intruduction/"
    content = urllib.request.urlopen(url).read().decode("utf-8")
    print(content)
    imagelist = re.findall('img src="(http.*?)"',content)
    print('共找到',len(imagelist),'张图片')
    saveimag(imagelist)


