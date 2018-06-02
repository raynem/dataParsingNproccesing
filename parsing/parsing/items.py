# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ParsingItem(scrapy.Item):
    id = scrapy.Field()
    theme = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    posts = scrapy.Field()
