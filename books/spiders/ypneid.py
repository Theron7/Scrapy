# -*- coding: utf-8 -*-
import scrapy


class YPspider(scrapy.Spider):
    name = "YPNE Interior Design"
    allowed_domains = ["yellowpages.com"]
    start_urls = ["https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=de",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=md",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=pa",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=nj",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=ny",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=ct",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=ri",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=ma",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=vt",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=nh",
    "https://www.yellowpages.com/search?search_terms=interior+decorators&geo_location_terms=me",

        ]


    
    def parse(self, response):
        for item_url in response.css("div.result h2.n a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_business_listing)
        next_page = response.css("div.pagination li a.next ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)     

    def parse_business_listing(self, response):
        item = {} 
        item["title"] =  response.css("#main-header h1 ::text").extract_first()
        item["phone number"] = response.css(".phone ::text").extract_first()
        item["address"] = response.css(".address ::text").extract()
        if response.css(".email-business"):
            item["email"] = response.css(".email-business").attrib["href"]
        if response.css(".primary-btn.website-link"):
            item["web address"] = response.css(".primary-btn.website-link").attrib["href"]
        item["fax Number"] = response.css("dd.extra-phones p:last-child span:last-child ::text").extract_first()
        item["Categories"] = response.css("dd.categories a ::text").extract()
        print(item)
        yield item
