#coding:utf8
import re
import urlparse
import urllib2
from bs4 import BeautifulSoup
import Spider_main
import urllib
import requests
class HtmlParser(object):
    count = 1
    def _get_new_urls(self, page_url, soup):
        print 'in parse def _get_new_urls'
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/xingganmote/'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
            #print 'new_full_url is '+new_full_url
        return new_urls

    def _get_new_data(self, page_url, soup):
        print 'in parse def _get_new_data'
        # <img src="http://img.1985t.com/uploads/attaches/2012/05/5324-CYyst1.jpg" onload="btnaddress(1);">
        pic_urls = soup.find_all('img', src=re.compile(r'http://img.1985t.com/uploads/attaches/'))
        #print "lenth = " + pic_urls.__len__()
        for pic_url in pic_urls:
            print pic_url['src']

            # 注意文件在命名保存时有些符号是不合法的！！！！！
            # 方法一
            #response = urllib2.urlopen(pic_url['src'])
            #print response.getcode()
            #with open("/Users/beyondwang/Desktop/%s.jpg" % str(Spider_main.obj_spider.count),'wb') as f:
                #f.write(response.read())
            #f.close()

            uname = str(HtmlParser.count)+'.jpg'
            HtmlParser.count += 1
            print uname
            # 方法二
            urllib.urlretrieve(pic_url['src'], uname)

            # 方法三
            #r = requests.get(pic_url['src'])
            #with open("da.jpg", "wb") as code:
                #code.write(r.content)

        print 'get_over'
        return

    def parse(self,page_url,html_cont):
        print "in html_parser def parse"
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        self._get_new_data(page_url,soup)

        print 'paser pver'
        return new_urls


