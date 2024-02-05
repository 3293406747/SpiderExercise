# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称+演员+上映时间
    name = scrapy.Field()
    star = scrapy.Field()
    time = scrapy.Field()
