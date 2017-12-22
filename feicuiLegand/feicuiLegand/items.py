# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeicuilegandItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FeucuiXinpin(scrapy.Item):
    table_name = scrapy.Field()
    acttitle = scrapy.Field()
    hhao = scrapy.Field()
    market_price = scrapy.Field()
    image_urls = scrapy.Field()
    desc = scrapy.Field()
    base_url = scrapy.Field()

class FeucuiSuggest(scrapy.Item):
    table_name = scrapy.Field()
    acttitle = scrapy.Field()
    hhao = scrapy.Field()
    market_price = scrapy.Field()
    image_urls = scrapy.Field()
    desc = scrapy.Field()
    video_url = scrapy.Field()
    base_url = scrapy.Field()
