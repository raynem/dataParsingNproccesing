# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from ..items import ParsingItem
from scrapy.linkextractors import LinkExtractor
import re


class CryptospiderSpider(CrawlSpider):
    name = 'CryptoSpider'
    allowed_domains = ['altcoincommunity.net']
    start_urls = ['https://altcoincommunity.net/forum-20.html']
    rules = (
        Rule(LinkExtractor(allow=('https://altcoincommunity.net/thread-\d+/',)), callback='parse'),
    )

    def parse(self, response):
        root = Selector(response)
        themes = root.css('.subject_new > a')
        for theme in themes:
            item = ParsingItem()
            link = theme.css('::attr(href)').extract()[0]
            item['theme'] = theme.css('::text').extract()[0]
            if link:
                yield scrapy.Request(response.urljoin(link), meta={'item':item} , callback=self.parse_links)

    def parse_links(self, response):
        item = response.meta['item']
        root = Selector(response)
        dates = root.css('.post_date')
        autors = root.css(".largetext > a")
        text = root.css(".post_body")
        texts, item['posts'] = [], []
        tmp = [i.css("::text").extract()[0] for i in autors]

        for i in text:
            i = ''.join(i.css('::text').extract())
            if i:
                i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags = re.MULTILINE)
                i = [s for s in i if s.isalpha() or s == ' ']
                texts.append(''.join(i))

        #texts = [x for x in texts if len(x)<=30]

        for it, date in enumerate(dates):
            item['posts'].append({'date': date.css("::text").extract()[0], 'author': tmp[it], 'text': texts[it]})
        yield item