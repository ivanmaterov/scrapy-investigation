import math

import scrapy
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.loader import ItemLoader

from grabber.items import DetailItem

DETAILS_PER_PAGE = 5


class QuotesSpider(scrapy.Spider):
    """Spider for mirasmart site."""
    name = "mirasmart"

    start_urls = ("https://index.mirasmart.com/AAN2020/SearchResults.php", )

    def parse(self, response: HtmlResponse) -> Request:
        """Entry parse function."""
        details_amount = int(response.xpath("//div[@class='full pagination offset']/p//text()").get().split(" ")[-1])
        page_amount = math.ceil(details_amount / DETAILS_PER_PAGE)
        for page in range(1, page_amount + 1):
            yield response.follow(
                url=f"?pg={page}",
                callback=self.parse_page,
            )

    def parse_page(self, response: HtmlResponse) -> Request:
        """Parse certain page."""
        search_results = response.xpath("//div[@class='full search-result']")
        abstract_link = search_results.xpath("ul[@class='downloads']/li/a/@href").getall()
        for num, details in enumerate(map(lambda elem: elem.xpath("div[@class='detail']"), search_results)):
            for detail in details:
                detail_item = ItemLoader(item=DetailItem(), selector=detail)
                detail_item.add_xpath(
                    "session_name",
                    "child::node()[3]/span//text()",
                )
                detail_item.add_xpath(
                    "topic",
                    "child::node()[5]/span/a//text()",
                )
                detail_item.add_xpath(
                    "program_number",
                    "child::node()[6]/span//text()",
                )

                yield response.follow(
                    url=abstract_link[num],
                    callback=self.parse_abstract_page,
                    cb_kwargs={"detail_item": detail_item},
                )

    def parse_abstract_page(
        self,
        response: HtmlResponse,
        detail_item: ItemLoader
    ) -> DetailItem:
        """Parse abstract page."""
        detail_item.add_value(
            "abstract",
            str(response.body),
        )
        yield detail_item.load_item()
