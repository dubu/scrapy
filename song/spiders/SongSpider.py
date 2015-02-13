# -*- coding: utf-8 -*-
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'song (+http://www.yourdomain.com)'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from song.items import SongItem


class SongSpider(CrawlSpider):
    name = 'song'
    allowed_domains = ['wikipedia.org']
    #start_urls = ['http://ko.wikipedia.org/wiki/송종국']
    #start_urls = ['http://ko.wikipedia.org/wiki/알베르트_리에라']
    #start_urls = ['http://ko.wikipedia.org/wiki/송종국', 'http://ko.wikipedia.org/wiki/박지성']
    start_urls = []
    with open('urls', 'r') as f:
        [start_urls.append(l.strip()) for l in f.readlines()]
    #start_urls = ['http://ko.wikipedia.org/wiki']
    #rules = [Rule(SgmlLinkExtractor(allow=['/송종국/']), 'parse')]
    #rules = [Rule(SgmlLinkExtractor(allow_domains=['/송종국/']), 'parse')]
    #rules = [Rule(SgmlLinkExtractor(allow=['/%EC%86%A1%EC%A2%85%EA%B5%AD/']), 'parse')]
    #rules = [Rule(SgmlLinkExtractor(allow_domains=['/%EC%86%A1%EC%A2%85%EA%B5%AD/']), 'parse')]
    def parse(self, response):
        sel = Selector(response)
        songItem = SongItem()
        songItem['url'] = response.url
        #songItem['nationality'] = sel.xpath("//div[@id='content']/div[@id='bodyContent']/div[@id='mw-content-text']/table[1]/tr[5]/td[2]/span[1]/a[1]/text()[1]").extract()[0]

        table = sel.xpath("//div[@id='content']/div[@id='bodyContent']/div[@id='mw-content-text']/table[1]")
        for tr in table.xpath('//tr'):
            if 0 < len(tr.xpath("td[@class='fn']")):
                songItem['name'] = tr.xpath("td[@class='fn']/text()[1]").extract()[0]
                continue
            cand = tr.xpath("td[1]/b[1]/text()[1]")
            print cand
            print cand.extract()
            if 0 == len(cand):    continue
            attr = cand.extract()[0]
            print attr
            if attr == u'국적':
                cand = tr.xpath("td[2]/span[@class='role']/a[1]/text()[1]")
                if 0 < len(cand):
                    songItem['nationality'] = cand.extract()[0]
            if attr == u'출생':
                cand = tr.xpath('td[2]/text()[1]')
                if 0 < len(cand):
                    songItem['birthday'] = cand.extract()[0]
                cand = tr.xpath('td[2]/p[1]')
                birthplace = ''
                for c in cand.xpath('a'):
                    birthplace += ' ' + c.xpath('text()[1]').extract()[0]
                songItem['birthplace'] = birthplace.strip()
            if attr == u'키':
                cand = tr.xpath('td[2]/text()[1]')
                if 0 < len(cand):
                    songItem['height'] = cand.extract()[0]
            if attr == u'체중':
                cand = tr.xpath('td[2]/text()[1]')
                if 0 < len(cand):
                    songItem['weight'] = cand.extract()[0]
            if attr == u'포지션':
                cand = tr.xpath("td[2]/span[@class='role']")
                positionCand = ''
                t = cand.xpath('text()[1]')
                if 0 < len(t):
                    positionCand = t.extract()[0].strip()
                    print positionCand
                for p in cand.xpath('a'):
                    positionCand += ' ' + p.xpath('text()[1]').extract()[0].strip()
                songItem['position'] = positionCand.strip()
            if attr == u'현 소속팀':
                cand = tr.xpath("td[2]/span[@class='org']/a[1]/text()[1]")
                if 0 < len(cand):
                    songItem['currentClub'] = cand.extract()[0]
            if attr == u'등번호':
                cand = tr.xpath('td[2]/text()[1]')
                if 0 < len(cand):
                    songItem['number'] = cand.extract()[0]
        open('test.song', 'wb').write(response.body)
        if 0 < len(cand):
            songItem['nationality'] = cand.extract()[0]
        if attr == u'출생':
            cand = tr.xpath('td[2]/text()[1]')
            if 0 < len(cand):
                songItem['birthday'] = cand.extract()[0]
            cand = tr.xpath('td[2]/p[1]')
            birthplace = ''
            for c in cand.xpath('a'):
                birthplace += ' ' + c.xpath('text()[1]').extract()[0]
            songItem['birthplace'] = birthplace.strip()
        if attr == u'키':
            cand = tr.xpath('td[2]/text()[1]')
            if 0 < len(cand):
                songItem['height'] = cand.extract()[0]
        if attr == u'체중':
            cand = tr.xpath('td[2]/text()[1]')
            if 0 < len(cand):
                songItem['weight'] = cand.extract()[0]
        if attr == u'포지션':
            cand = tr.xpath("td[2]/span[@class='role']")
            positionCand = ''
            t = cand.xpath('text()[1]')
            if 0 < len(t):
                positionCand = t.extract()[0].strip()
                print positionCand
            for p in cand.xpath('a'):
                positionCand += ' ' + p.xpath('text()[1]').extract()[0].strip()
            songItem['position'] = positionCand.strip()
        if attr == u'현 소속팀':
            cand = tr.xpath("td[2]/span[@class='org']/a[1]/text()[1]")
            if 0 < len(cand):
                songItem['currentClub'] = cand.extract()[0]
        if attr == u'등번호':
            cand = tr.xpath('td[2]/text()[1]')
            if 0 < len(cand):
                songItem['number'] = cand.extract()[0]
        open('test.song', 'wb').write(response.body)
        print songItem['url']
        print songItem['name']
        if 'nationality' in songItem:    print songItem['nationality'], type(songItem['nationality'])
        if 'birthday' in songItem:    print songItem['birthday']
        if 'birthplace' in songItem:    print songItem['birthplace']
        if 'height' in songItem:    print songItem['height']
        if 'weight' in songItem:    print songItem['weight']
        if 'position' in songItem:    print songItem['position']
        if 'currentClub' in songItem:    print songItem['currentClub']
        if 'number' in songItem:    print songItem['number']
        return songItem