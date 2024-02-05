import scrapy
from ..items import DaomubijiItem


class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response, **kwargs):
        a_list = response.xpath('//li[contains(@class,"menu-item")]/a')
        for a in a_list:
            item = DaomubijiItem()
            item["title"] = a.xpath('./text()').get()
            link = a.xpath('./@href').get()
            yield scrapy.Request(link,callback=self.parse_two_page, meta={"item": item})

    def parse_two_page(self, response):
        item = response.meta["item"]
        a_list = response.xpath('//article/a')
        for a in a_list:
            sub_title = a.xpath('./text()').get().replace("?", "？")
            link = a.xpath('./@href').get()
            yield scrapy.Request(link, callback=self.parse_three_page, meta={"item": item, "sub_title": sub_title})

    def parse_three_page(self, response):
        item = response.meta["item"]
        item["sub_title"] = response.meta["sub_title"]
        p_list = response.xpath('//article/p/text()').extract()
        item["content"] = "\n".join(p_list)
        yield item
