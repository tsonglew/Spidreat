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
        for each in response.xpath('//div[@class="post-meta"]/p'):
            try:
                time = each.xpath('text()').extract()[1].strip()[:10]
                item = JobboleItem()
                item['title'] = each.xpath('a[@class="meta-title"]/@title').extract()
                item['link'] = each.xpath('a[@class="meta-title"]/@href').extract()
                item['timestamp'] = time
                item['tag'] = 'JobbolePython'
                yield item
            except IndexError:
                continue
