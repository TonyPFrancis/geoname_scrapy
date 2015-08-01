__author__ = 'tony'
from scrapy.spider import Spider
from scrapy.log import ScrapyFileLogObserver
from scrapy import log
from scrapy import Selector
from geoname.settings import *
import requests
import os

class GeonameSpider(Spider):
    name = 'geoname'
    start_urls = ['http://download.geonames.org/export/dump/',]
    allowed_domains = ['geonames.org',]

    def parse(self, response):
        sel = Selector(response)
        if not os.path.exists(ROOT_FOLDER):
            os.mkdir(ROOT_FOLDER)

        FILE_XPATH = '//pre[a]/a/@href'

        file_links = sel.xpath(FILE_XPATH).extract()
        if file_links:
            for file_link in file_links:
                file_link = response.url+file_link
                if '.' in file_link.split('/')[-1]:
                    file_name = file_link.split('/')[-1]
                    file_path = os.path.join(ROOT_FOLDER, file_name)
                    print "FECTHING %s"%(file_name)
                    try:
                        f = open(file_path,'w+')
                        f.write(requests.get(url=file_link).content)
                        f.close()
                        print 'SAVED AT %s'%(file_path)
                    except:
                        print 'FETCH ERROR AT FILE %s'%(file_name)
        else:
            return

