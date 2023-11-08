import scrapy


class AmazonBotSpider(scrapy.Spider):
    name = "amazon-bot"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
