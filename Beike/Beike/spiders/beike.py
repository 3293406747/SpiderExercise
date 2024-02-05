import re

import scrapy
from ..items import BeikeItem

from urllib import parse
import requests
from fake_useragent import UserAgent

class BeikeSpider(scrapy.Spider):
    name = 'beike'
    allowed_domains = ['km.ke.com']
    words = input("请输入区域或小区名称：")
    one_url = 'https://km.ke.com/ershoufang/pg{}sf1rs{}/'

    def start_requests(self):
        words = parse.quote(self.words)
        url = self.one_url.format(1,words)
        total_page = self.get_total_page(url)
        for i in range(total_page):
            url = self.one_url.format(i+1,self.words)
            yield scrapy.Request(url=url,callback=self.parse)


    def get_total_page(self, url):
        ua = UserAgent()
        headers = {"User-Agent": ua.random}
        response = requests.get(url, headers=headers)
        c = re.compile('"totalPage":(.*?),')
        total_page = c.search(response.text).group(1)
        return int(total_page)


    def parse(self, response, **kwargs):
        item = BeikeItem()
        a_list = response.xpath("//ul//div[@class='title']/a")
        for a in a_list:
            fb_expo_id = a.xpath("./@data-maidian").get()
            href = a.xpath("./@href").get()
            link = "{}?fb_expo_id={}".format(href, str(fb_expo_id))
            yield scrapy.Request(url=link, callback=self.parse_inner_page, meta={"item": item})

    def parse_inner_page(self, response):
        item = response.meta["item"]
        area = response.xpath("//span[text()='建筑面积']/../text()").extract()
        item["house_area"] = float(area[1].strip().replace("㎡", "")) if len(area) == 2 else None
        floor = response.xpath("//span[text()='所在楼层']/../text()").extract()
        item["house_floor"] = floor[1].strip() if len(floor) >= 2 else None
        type_ = response.xpath("//span[text()='房屋户型']/../text()").extract()
        item["house_type"] = type_[1].strip() if len(type_) == 2 else None
        price = response.xpath("//span[@class='unitPriceValue']/text()").extract()
        item["house_price"] = float(price[0]) if len(price) == 1 else None
        region_list = response.xpath("//div[@class='areaName']//a/text()").extract()
        region = "·".join(region_list)
        item["house_region"] = region if region else None
        name = response.xpath("//a[@class='info no_resblock_a']/text()").extract()
        item["region_name"] = name[0] if len(name) == 1 else None
        yield item

