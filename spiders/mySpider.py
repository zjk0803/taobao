# -*- coding: utf-8 -*-


from time import sleep
import time
import random
from pyquery import PyQuery as pq

from scrapy import Request,Spider
from urllib.parse import quote
from taobao.items import TaobaoItem

from scrapy import Spider,Request
from selenium import webdriver
class loginTB(Spider):
    name = 'taobao'

    def __init__(self):
        self.browser = webdriver.Chrome("D:\google浏览器\Application\chromedriver1.exe")
        self.browser.set_page_load_timeout(30)

    #def closed(self, spider):
    #    print("spider closed")
    #    self.browser.close()

    def start_requests(self):
        start_urls = [
            'https://s.taobao.com/search?q=ipad'.format(
                str(i)) for i in range(1, 150, 2)]
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"]//div[contains(@class,"item")]')
        for product in products:
            item = TaobaoItem()
            item['price'] = ''.join(product.xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()
            #item['image'] = ''.join(product.xpath('.//div[@class="pic"]//img=[contains(@class,"img")]/@data=src').extract()).strip()
            item['deal'] = product.xpath('.//div[contains(@class,"deal-cnt")]//text()').extract_first()
            item['location'] = product.xpath('.//div[contains(@class,"location")]//text()').extract_first()
            yield item

        print(len(products))
        print('---------------------------------------------------')

    '''allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='
    def start_requests(self):
        for keyword in self.settings.get('KEYWORD'):
            for page in range(1,self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield Request(url=url,callback=self.parse,meta={'page':page},dont_filter=True)
    def parse(self, response):
        products = response.xpath('//div[@id=mainsrp-itemlist]//div[@class="items"][1]//div[contains(@class,"item")]')
        for product in products:
            item = TaobaoItem()
            item['price']=''.join(product.xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()
            item['image'] = ''.join(product.xpath('.//div[@class="pic"]//img=[contains(@class,"img")]/@data=src').extract()).strip()
            item['deal'] = product.xpath('.//div[contains(@class,"deal-cnt")]//text()').extract_first()
            item['location'] = product.xpath('.//div[contains(@class,"location")]//text()').extract_first()
            yield item
'''



