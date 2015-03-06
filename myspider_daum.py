__author__ = 'dubu9'

from scrapy import Spider, Item, Field

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from song.items import SongItem


class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = 'blogspider', ['http://www.daum.net']

    def parse(self, response):
        sel = Selector(response)
        #print sel.xpath(/html/body/center/table/tbody/tr/td[2]/table/tbody/tr/td/form/table[2]/tbody/tr/td[3]
        print '##############'
        print sel.xpath('/html/body/div[3]/main/article/div/div/div/div/div/ul/li')
        #return [Post(title=e.extract()) for e in response.css("h2 a::text")]
        return [Post(title=e.extract()) for e in response.css("h2 a::text")]
    
