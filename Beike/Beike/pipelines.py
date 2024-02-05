# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BeikePipeline:
    def process_item(self, item, spider):
        print(item["house_area"])
        print(item["house_floor"])
        print(item["house_type"])
        print(item["house_price"])
        print(item["house_region"])
        print(item["region_name"])
        return item
