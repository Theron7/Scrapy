# -*- coding: utf-8 -*-
import scrapy


class Asidspider(scrapy.Spider):
    name = "ASID Interior Design"
    allowed_domains = ["asid.org"]
    start_urls = ["https://www.asid.org/find-a-pro?zip=&zip_radius=100&display_name=&business_name=&project_types=&project_types%5B%5D=HOME" ]


    
    def parse(self, response):
        for item_url in response.css("div.fapip-index-results a.fapip-abstract ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_business_listing)
        next_page = response.css("div.fapip-index-pagination li.next a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)     

    def parse_business_listing(self, response):
        item = {} 
        item["title"] =  response.css("h1.fapip-view-header-title ::text").extract_first()
        # item["phone number"] = response.css(".phone ::text").extract_first()
        # item["address"] = response.css(".address ::text").extract()
        # if response.css(".email-business"):
        #     item["email"] = response.css(".email-business").attrib["href"]
        # if response.css(".primary-btn.website-link"):
        #     item["web address"] = response.css(".primary-btn.website-link").attrib["href"]
        # item["fax Number"] = response.css("dd.extra-phones p:last-child span:last-child ::text").extract_first()
        # item["Categories"] = response.css("dd.categories a ::text").extract()
        print(item)
        yield item