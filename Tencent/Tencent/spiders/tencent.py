import scrapy
from urllib import parse
import requests
import json
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_page_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword={}&pageIndex={}&pageSize=10'
    two_page_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}'
    keyword = input("请输入关键字:")

    def start_requests(self):
        keyword = parse.quote(str(self.keyword))
        count = self.get_total(keyword)
        for i in range(count):
            yield scrapy.Request(self.one_page_url.format(keyword,i+1), callback=self.parse)

    def get_total(self, keyword):
        url = self.one_page_url.format(keyword, 1)
        response = requests.get(url)
        count = response.json()["Data"]["Count"]
        return count // 10 if count % 10 == 0 else count // 10 + 1

    def parse(self, response, **kwargs):
        item = TencentItem()
        posts = json.loads(response.text)["Data"]["Posts"]
        for post in posts:
            post_id = post["PostId"]
            yield scrapy.Request(self.two_page_url.format(post_id), callback=self.parse_two_page, meta={"item": item})

    def parse_two_page(self, response):
        item = response.meta["item"]
        data = json.loads(response.text)["Data"]
        item["job_name"] = data["RecruitPostName"]
        item["job_type"] = data["CategoryName"]
        item["job_duty"] = data["Responsibility"]
        item["job_require"] = data["Requirement"]
        item["job_address"] = data["LocationName"]
        item["job_time"] = data["LastUpdateTime"]
        yield item


