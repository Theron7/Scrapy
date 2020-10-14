# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.theluxuryartmepra.com"]
    start_urls = [
        'https://www.theluxuryartmepra.com/flatware/art/',
        #"https://www.theluxuryartmepra.com/flatware/titanium/",
        #"https://www.theluxuryartmepra.com/flatware/stainless-steel/",
        #"https://www.theluxuryartmepra.com/flatware/vintage/",
        #"https://www.theluxuryartmepra.com/flatware/epoque/",
        #"https://www.theluxuryartmepra.com/flatware/fantasia/",
        
    ]

    def parse(self, response):
        for item_url in response.css("ul.products-grid > li.item > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_book_page)
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = {}
        product = response.css("div.product-shop")
        item["title"] = product.css(".product-name h1 ::text").extract_first()
        item["number"] = product.css(".product-name span.sku ::text").extract_first()
        item['price'] = product.css(".price-info .price-box span.price ::text").extract_first()
        #item["image"] = product.css(".img class .src=::image").extract_first()
        yield item
