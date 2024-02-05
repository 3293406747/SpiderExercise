# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TencentPipeline:
    def process_item(self, item, spider):
        print(item["job_name"])
        print(item["job_type"])
        print(item["job_duty"])
        print(item["job_require"])
        print(item["job_address"])
        print(item["job_time"])
        return item
