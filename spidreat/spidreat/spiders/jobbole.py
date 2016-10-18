# -*- coding: utf-8 -*-

import scrapy

from spidreat.items import JobboleItem

class JobbolePythonSpider(scrapy.Spider):
    name = "jobbolepython"
    allowed_domains = ["jobbole.com"]
    start_urls = [
            "http://python.jobbole.com/",
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

class JobboleFrontSpider(scrapy.Spider):
    name = "jobboleweb"
    allowed_domains = ["jobbole.com"]
    start_urls = [
            "http://web.jobbole.com/"
            ]
    def parse(self, response):
        for each in response.xpath('//div[@class="post-meta"]/p'):
            try:
                time = each.xpath('text()').extract()[1].strip()[:10]
                item = JobboleItem()
                item['title'] = each.xpath('a[@class="meta-title"]/@title').extract()
                item['link'] = each.xpath('a[@class="meta-title"]/@href').extract()
                item['timestamp'] = time
                item['tag'] = 'JobboleFront'
                yield item
            except IndexError:
                continue

class JobboleJavaSpider(scrapy.Spider):
    name = "jobbolejava"
    allowed_domains = ["importnew.com"]
    start_urls = [
            "http://www.importnew.com/"
            ]
    def parse(self, response):
        for each in response.xpath('//div[@class="post-meta"]/p'):
            try:
                time = each.xpath('text()').extract()[1].strip()[:10]
                item = JobboleItem()
                item['title'] = each.xpath('a[@class="meta-title"]/@title').extract()
                item['link'] = each.xpath('a[@class="meta-title"]/@href').extract()
                item['timestamp'] = time
                item['tag'] = 'JobboleJava'
                yield item
            except IndexError:
                continue

class JobboleAndroidSpider(scrapy.Spider):
    name = "jobboleandroid"
    allowed_domains = ["jobbole.com"]
    start_urls = [
            "http://android.jobbole.com/"
            ]
    def parse(self, response):
        for each in response.xpath('//div[@class="post-meta"]/p'):
            try:
                time = each.xpath('text()').extract()[1].strip()[:10]
                item = JobboleItem()
                item['title'] = each.xpath('a[@class="meta-title"]/@title').extract()
                item['link'] = each.xpath('a[@class="meta-title"]/@href').extract()
                item['timestamp'] = time
                item['tag'] = 'JobboleAndroid'
                yield item
            except IndexError:
                continue

class JobboleIOSSpider(scrapy.Spider):
    name = "jobboleios"
    allowed_domains = ["jobbole.com"]
    start_urls = [
            "http://ios.jobbole.com/"
            ]
    def parse(self, response):
        for each in response.xpath('//div[@class="post-meta"]/p'):
            try:
                time = each.xpath('text()').extract()[1].strip()[:10]
                item = JobboleItem()
                item['title'] = each.xpath('a[@class="meta-title"]/@title').extract()
                item['link'] = each.xpath('a[@class="meta-title"]/@href').extract()
                item['timestamp'] = time
                item['tag'] = 'JobboleIOS'
                yield item
            except IndexError:
                continue
