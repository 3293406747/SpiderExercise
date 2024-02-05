# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 目录名+文件名+小说内容
    title = scrapy.Field()
    sub_title = scrapy.Field()
    content = scrapy.Field()
