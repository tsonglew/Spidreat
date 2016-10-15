# -*- coding: utf-8 -*-

import scrapy

from spidreat.items import SegmentFaultItem


class SegmentFaultSpider(scrapy.Spider):
    name = "segmentfaultpython"
    allowed_domains = ["segmentfault.com"]
    start_urls = [
            "https://segmentfault.com/t/python/blogs"
            ]

    def parse(self, response):
        for each in 
            try:

                yield item
            except IndexError:
                continue
