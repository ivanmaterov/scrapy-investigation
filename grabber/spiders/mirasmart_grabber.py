import scrapy


class QuotesSpider(scrapy.Spider):
    name = "mirasmart"

    start_urls = ("https://index.mirasmart.com/AAN2020/SearchResults.php", )

    def parse(self, response):
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
        
        pagination_div = response.xpath("//div[@class='full pagination offset']")
        # if there is the next page
        if pagination_div.xpath("ul/li[last()]//child::i").get():
            next_page = pagination_div.xpath("ul/li[last()]/a/@href").get()
            yield response.follow(
                url=next_page,
                callback=self.parse,
            )

    def parse_abstract_page(self, response, event_details):
        event_details["abstract"] = str(response.body)
        yield event_details
