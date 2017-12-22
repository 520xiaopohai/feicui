# -*- coding: utf-8 -*-
import scrapy
from urllib import parse as urlparse
import re
from feicuiLegand.items import FeucuiSuggest
class OwnersuggestSpider(scrapy.Spider):
    name = 'ownerSuggest'
    start_urls = ['https://www.jaadee.com/feicuipifa/']

    def parse(self, response):
        # print(response)
        product_url_nodes = response.xpath('/html/body/div[5]/div[2]/ul/li/a/@href').extract()

        for product_url_node in product_url_nodes:
            print(product_url_node)
            yield scrapy.Request(url=urlparse.urljoin(response.url, product_url_node), callback=self.parse_product)

        next_page_url = response.css(
            u'div.pagenavi a:contains("下一页")::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(
                url=urlparse.urljoin("https://www.jaadee.com", next_page_url),
                callback=self.parse)
        pass

    def parse_product(self, response):
        item = FeucuiSuggest()
        item['base_url'] = response.url
        item['table_name'] = 'suggest'
        item['acttitle'] = response.xpath('/html/body/div[5]/div[3]/div[2]/h3/text()').extract_first()
        huohao = response.xpath('//span[@class="hhao"]/text()').extract_first()
        match_hhao_re = re.match(r".*?(\w+\d+).*", huohao)
        if match_hhao_re:
            item['hhao'] = match_hhao_re.group(1)
        else:
            item['hhao'] = "0"

        money_arr = response.xpath('/html/body/div[5]/div[3]/div[2]/ul/li[3]/span/text()')
        money = money_arr.extract_first() if len(money_arr)>0 else '0'
        match_price_re = re.match(r".*?(\d+).*", money)
        if match_price_re:
            item['market_price'] = match_price_re.group(1)
        else:
            item['market_price'] = "0"

        image_urls = ','.join(response.xpath('//*[@id="actul"]/li/a/img/@src').extract())
        item['image_urls'] = image_urls
        desc = '.'.join(response.xpath('//*[@id="act_tab_1"]/div/text()').extract()).strip()
        item['desc'] = desc

        video_arr = response.xpath('//*[@id="example_video_1"]/source/@src')
        video_url= video_arr.extract_first() if len(video_arr)>0 else ''
        item['video_url'] = video_url
        yield item