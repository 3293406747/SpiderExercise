# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path


class DaomubijiPipeline:
    def process_item(self, item, spider):
        print(item["title"])
        print(item["sub_title"])
        print(item["content"])
        return item

class DaomubijiFilePipeline:
    def process_item(self, item, spider):
        path = Path(__file__).resolve().parent.parent.joinpath("downloads", item["title"])
        path.mkdir(parents=True, exist_ok=True)
        with path.joinpath('{}.txt'.format(item["sub_title"])).open(mode="w",encoding="utf-8") as f:
            f.write(item["content"])
        return item
