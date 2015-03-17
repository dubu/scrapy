__author__ = 'dubu9'

from scrapy import Spider, Item, Field

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from song.items import SongItem
import MySQLdb


class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = 'blogspider', ['http://www.daum.net']

    def parse(self, response):
	db=MySQLdb.connect(user='scrapy', passwd='scrapy', db='scrapy')
	c=db.cursor()
        sel = Selector(response)
        #print sel.xpath(/html/body/center/table/tbody/tr/td[2]/table/tbody/tr/td/form/table[2]/tbody/tr/td[3]
        print '##############'
        #print sel.xpath('/html/body/div[3]/main/article/div/div/div/div/div/ul/li')
        #return [Post(title=e.extract()) for e in response.css("h2 a::text")]
	# real time issute
	#for e in sel.xpath('/html/body/div[3]/main/article/div/div/div/div[2]/div/ol/li[6]/div/div/span[2]/a/text()[1]').extract()[0]:
	for e in sel.xpath('/html/body/div[3]/main/article/div/div/div/div[2]/div/ol/li'):
		title = e.xpath('div/div/span[2]/a/text()[1]').extract()[0]
		#c.execute(""" insert into hs_event(title,cont_img_url) values ('kong','c') """)
		print c.execute(""" insert into hs_event(title,cont_img_url) values ('"""+title.encode('utf-8')+"""','none') """)
		#print c.execute(""" insert into hs_event(title,cont_img_url) values ('cccccccccccccc','nnnn') """)
		print title
	db.commit()
        return [Post(title=e) for e in sel.xpath('/html/body/div[3]/main/article/div/div/div/div[2]/div/ol/li[6]/div/div/span[2]/a/text()[1]').extract()[0]]
        #return [Post(title=e.xpath('/div/div/span[2]/a/text()[1]') ) for e in sel.xpath('/html/body/div[3]/main/article/div/div/div/div[2]/div/ol/li')]
    
