import scrapy
from ..items import AmazonScraperAlertSystemItem

class AmazonBotSpider(scrapy.Spider):
    name = "amazon-bot"
    # allowed_domains = ["example.com"]
    start_urls = [
        "https://www.amazon.in/s?k=mobile"
    ]

    def parse(self, response):
        # product = AmazonScraperAlertSystemItem()
        # response.css(".a-size-medium.a-text-normal::text").extract()
        name = response.css(".a-color-base.a-text-normal::text").extract()
        image_urls = response.css(".s-image::attr(src)").extract()
        # yield AmazonScraperAlertSystemItem(title = title.strip(), brand = brand.strip(), rating = rating.strip(), price = price.strip(), colour = colour.strip(), instock = instock, reviews = reviews, description = description, image_urls = [img_url])
        # product['name'] = name
        # product['image_urls'] = image_urls
        print(name, image_urls)
        yield AmazonScraperAlertSystemItem(name = name, image_urls = image_urls)