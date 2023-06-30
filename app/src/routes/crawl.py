from flask import Blueprint, Flask, request, url_for, redirect
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings

from src.consts import consts as C
from src.services.spiders.quasarzone_spider import QuasarzoneSpider 

routes = Blueprint("crawl", __name__, url_prefix="/crawl")


@routes.route('/<string:website>' ,methods=['GET'])
def crawl_website(website):
    if website == C.WebsiteName.CLIEN:
        run_spider(QuasarzoneSpider)
    elif website == C.WebsiteName.QUASARZONE:
        run_spider(QuasarzoneSpider)
    elif website == C.WebsiteName.PPOMPPU:
        run_spider(QuasarzoneSpider)
    elif website == C.WebsiteName.DEALBADA:
        run_spider(QuasarzoneSpider)
    elif website == C.WebsiteName.RULIWEB:
        run_spider(QuasarzoneSpider)
    elif website == C.WebsiteName.FMKOREA:
        run_spider(QuasarzoneSpider)
    else :
        return "Not supported website: " + website    
    # return "Crawling website: " + website



def run_spider(spider):
    process = CrawlerProcess(get_scrapy_settings())
    result = []    
    def collect_results(item, reponse, spider):
        result.append(item)
    process.crawl(spider, callback=collect_results)
    process.start()  # the script will block here until the crawling is finished
    return result


def get_scrapy_settings():
    settings = Settings()
    settings.set("REQUEST_FINGERPRINTER_IMPLEMENTATION", "2.7")
    settings.set("FEED_EXPORT_ENCODING", "utf-8")
    return settings
