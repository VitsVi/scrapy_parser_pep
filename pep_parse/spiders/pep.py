from urllib.parse import urljoin

import scrapy

from pep_parse.constants import PEPS_URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/numerical/"]

    def parse(self, response):
        for tr_tag in response.css('tr'):
            a_href = (tr_tag.css('a::attr(href)').get())
            pep_page_link = urljoin(PEPS_URL, a_href)
            yield response.follow(
                pep_page_link,
                callback=self.parse_pep,
            )

    def parse_pep(self, response):
        status = None
        name = response.xpath(
            "substring-after(//h1[@class='page-title']/text(), ' – ')"
        ).get()
        number = response.xpath(
            "(substring-before(substring-after"
            "(//h1[@class='page-title']/text(), 'PEP '), ' – '))"
        ).get()
        status = response.css("abbr::text").get()

        yield PepParseItem({
            "number": number,
            "name": name,
            "status": status
        })
