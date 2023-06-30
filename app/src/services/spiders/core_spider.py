import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from pathlib import Path
from consts import consts as C
from scrapy.utils.log import configure_logging

class CoreSpider(scrapy.Spider):
    name = C.WebsiteName.QUASARZONE
    
    start_urls = [
        C.WebsiteUrl.QUASARZONE_URL
    ]

    def parse(self, response):
        # response == crwaled html data
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        yield {'body' : response.body}
        
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

runner = CrawlerRunner()
deferred = runner.crawl(QuasarzoneSpider)
deferred.addBoth(lambda _: reactor.stop())
reactor.run()
