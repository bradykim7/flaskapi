import scrapy
from scrapy.crawler import CrawlerProcess
from pathlib import Path
from consts import consts as C

class QuasarzoneSpider(scrapy.Spider):
    name = "quasarzone"
    name = C.WebsiteName.QUASARZONE

    # def start_requests(self):
    #     urls = [
    #         const.WebsiteUrl.QUASARZONE_URL,
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    
    # substitute for start_requests same as above
    start_urls = [
        C.WebsiteUrl.QUASARZONE_URL
    ]

    def parse(self, response):
        # response == crwaled html data
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")