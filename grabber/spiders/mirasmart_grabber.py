import math
import scrapy


DETAILS_PER_PAGE = 5

class QuotesSpider(scrapy.Spider):
    """Spider for mirasmart site."""
    name = "mirasmart"

    start_urls = ("https://index.mirasmart.com/AAN2020/SearchResults.php", )

    def parse(self, response):
        """Entry parse function."""
        details_amount = int(response.xpath("//div[@class='full pagination offset']/p//text()").get().split(" ")[-1])
        page_amount = math.ceil(details_amount / DETAILS_PER_PAGE)
        for page in range(1, page_amount + 1):
            yield response.follow(
                url=f"?pg={page}",
                callback=self.parse_page,
            )

    def parse_page(self, response):
        """Parse certain page."""
        search_results = response.xpath("//div[@class='full search-result']")
        abstract_link = search_results.xpath("ul[@class='downloads']/li/a/@href").getall()
        for num, details in enumerate(map(lambda elem: elem.xpath("div[@class='detail']"), search_results)):
            for detail in details:
                event_details = {
                    "session_name": detail.xpath("child::node()[3]/span//text()").get(),
                    "topic": detail.xpath("child::node()[5]/span/a//text()").get(),
                    "program_number": detail.xpath("child::node()[6]/span//text()").get(),
                }
                yield response.follow(
                    url=abstract_link[num],
                    callback=self.parse_abstract_page,
                    cb_kwargs={"event_details": event_details},
                )

    def parse_abstract_page(self, response, event_details):
        """Parse abstract page."""
        event_details["abstract"] = str(response.body)
        yield event_details
