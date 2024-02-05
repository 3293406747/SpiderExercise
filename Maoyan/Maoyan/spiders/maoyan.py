import re

import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']

    def start_requests(self):
        for offset in range(0,91,10):
            url = 'https://www.maoyan.com/board/4?offset={}'.format(offset)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response, **kwargs):
        print(response.url)
        item = MaoyanItem()
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            response = dd.xpath('.//div[@class="movie-item-info"]/p[@class="name"]/a/text()').get()
            item["name"] = response.strip() if response else None
            response = dd.xpath('.//div[@class="movie-item-info"]/p[@class="star"]/text()').get()
            item["star"] = response.replace("主演：", "").strip() if response else None
            response = dd.xpath('.//div[@class="movie-item-info"]/p[@class="releasetime"]/text()').get()
            item["time"] = re.compile("\d*-?\d*-?\d+").search(response).group(0) if response else None
            yield item