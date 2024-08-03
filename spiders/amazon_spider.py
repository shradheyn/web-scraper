import scrapy
from ..items import AmazonscrapItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&qid=1689487738&rnid=2684818031&ref=lp_976390031_nr_p_n_publication_date_0'
    ]

    def parse(self, response, **kwargs):
        items = AmazonscrapItem()

        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-row .a-size-base:nth-child(2)').css('::text').extract()
        product_price = response.css('.puis-price-instructions-style .a-price-whole').css('.a-price-whole::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name']=product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
