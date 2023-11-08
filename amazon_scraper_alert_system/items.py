# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperAlertSystemItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # title = scrapy.Field()
    # brand = scrapy.Field()
    # rating = scrapy.Field()
    # price = scrapy.Field()
    # colour = scrapy.Field()
    # instock = scrapy.Field()
    # reviews = scrapy.Field()
    # description = scrapy.Field()
    image_urls = scrapy.Field()
    # images = scrapy.Field()
