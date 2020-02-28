import scrapy


class quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        for quote in response.xpath('.//*[@class="quote"]'):
            text = quote.xpath('.//*[@class="text"]/text()').extract_first(),
            author = quote.xpath(
                './/*[@class="author"]/text()').extract_first(),
            keywords = quote.xpath(
                './/*[@class="keywords"]/@content').extract_first(),

            yield {
                "Text": text,
                "Author": author,
                "Keywords": keywords
            }
