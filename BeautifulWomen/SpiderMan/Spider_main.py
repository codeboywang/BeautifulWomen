import url_manager  , html_parser , html_downloader

class Spider_main(object):
    count = 1
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d:%s" % (Spider_main.count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                if Spider_main.count == 66:
                    break;
                Spider_main.count += 1
            except:
                print "crow failed"


if __name__ == "__main__":
    print Spider_main.count
    root_url = "http://www.4493.com/xingganmote/5433/1.htm"
    obj_spider = Spider_main()
    obj_spider.craw(root_url)
