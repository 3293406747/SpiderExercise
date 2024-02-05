# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeItem(scrapy.Item):
    # define the fields for your item here like:
    # 面积+楼层+户型+单价+区域+小区名称
    house_area = scrapy.Field()
    house_floor = scrapy.Field()
    house_type = scrapy.Field()
    house_price = scrapy.Field()
    house_region = scrapy.Field()
    region_name = scrapy.Field()
