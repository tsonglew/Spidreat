# -*- coding: utf-8 -*-

import scrapy

from spidreat.items import SegmentFaultItem


class SegmentFaultPythonSpider(scrapy.Spider):
    name = "segmentfaultpython"
    allowed_domains = ["segmentfault.com"]
    start_urls = [
            "https://segmentfault.com/t/python/blogs"
            ]

    def parse(self, response):
        for each in response.xpath('//div[@class="summary"]'):
            try:
                time = each.xpath('ul/li/text()').extract()[3].strip()
                item = SegmentFaultItem()
                item['title'] = each.xpath('h2/a/text()').extract()
                item['link'] = ''.join(['https://segmentfault.com/', each.xpath('h2/a/@href').extract()[0]])
                item['timestamp'] = time
                item['tag'] = 'SegmentFaultPython'
                yield item
            except IndexError:
                continue
