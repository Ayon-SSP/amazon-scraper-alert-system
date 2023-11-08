import scrapy
from ..items import AmazonScraperAlertSystemItem

class AmazonBotSpider(scrapy.Spider):
    name = "amazon-bot"
    # allowed_domains = ["example.com"]
    start_urls = [
        "https://www.amazon.in/s?k=mobile"
    ]

    def parse(self, response):
        # # product = AmazonScraperAlertSystemItem()
        # # response.css(".a-size-medium.a-text-normal::text").extract()
        # name = response.css(".a-color-base.a-text-normal::text").extract()
        # image_urls = response.css(".s-image::attr(src)").extract()
        # # yield AmazonScraperAlertSystemItem(title = title.strip(), brand = brand.strip(), rating = rating.strip(), price = price.strip(), colour = colour.strip(), instock = instock, reviews = reviews, description = description, image_urls = [img_url])
        # # product['name'] = name
        # # product['image_urls'] = image_urls
        # print(name, image_urls)
        # # yield AmazonScraperAlertSystemItem(name = name, image_urls = image_urls)




        title = response.css(".a-color-base.a-text-normal::text").extract() or response.css(".a-size-medium.a-text-normal::text").extract()
        brand = response.xpath("//a[@id='bylineInfo']//text()").get() or "not specified"
        # rating = response.xpath("//div[@id='averageCustomerReviews_feature_div']").xpath("//span[@class='a-icon-alt']//text()").get()

        # price = response.xpath("//span[@id='priceblock_ourprice']//text()") or response.xpath("//span[@id='priceblock_dealprice']//text()")
        # print(price)
        # if len(price) > 1: price = price[1].get()
        # elif len(price) == 1: price = price[0].get()
        # else : price = price.get()

        # colour = response.xpath("//div[@id='variation_color_name']/div/span[@class='selection']//text()").get() or "not defined"
        # instock = response.xpath("//div[@id='availability']").xpath("//span[@class='a-size-medium a-color-success']//text()").get() or "Out Stock"
        # instock = instock.strip() == "In stock."
        # reviews = response.xpath("//div[@class='a-expander-content reviewText review-text-content a-expander-partial-collapse-content']/span//text()").getall()
        # description_raw = response.xpath("//div[@id='featurebullets_feature_div']//span[@class='a-list-item']//text()").getall()

        img_url = response.css(".s-image::attr(src)").extract()

        # description = []
        # for description_temp in description_raw:
        #     description.append(description_temp.strip())



        # print(title, brand, rating, price, colour, instock, img_url)
        yield AmazonScraperAlertSystemItem(title = title, brand = brand.strip(), image_urls = img_url)
        # yield AmazonScraperAlertSystemItem(title = title.strip(), brand = brand.strip(), rating = rating.strip(), price = price.strip(), colour = colour.strip(), instock = instock, reviews = reviews, description = description, image_urls = [img_url])