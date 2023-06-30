import scrapy
from pathlib import Path
from src.consts import consts as C

class QuasarzoneSpider(scrapy.Spider):
    name = C.WebsiteName.QUASARZONE
    
    start_urls = [
        C.WebsiteUrl.QUASARZONE_URL
    ]

    def parse(self, response):
        yield {'body' : response.body}
