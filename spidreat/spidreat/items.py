# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidreatItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobboleItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()
    tag = scrapy.Field()

class SegmentFaultItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()
    tag = scrapy.Field()
