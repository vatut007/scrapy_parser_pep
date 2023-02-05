import re

import scrapy

from pep_parse.constants import PATTERN_PEP
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.xpath(
            '//a[@class="pep reference internal"]/@href').getall()
        for group_link in all_pep:
            yield response.follow(group_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_match = re.search(PATTERN_PEP, response.css(
            'h1.page-title::text').get())
        data = {
            'number': pep_match.group('number'),
            'name': pep_match.group('name'),
            'status': response.css('dt:contains("Status") + dd ::text').get(),
        }
        yield PepParseItem(data)
