import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MySpider(CrawlSpider):
    name = 'my_spider'
    allowed_domains = ['xcelore.com']
    start_urls = ['https://xcelore.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log(f'Visited: {response.url}')

        yield {
            'url': response.url,
            'title': response.css('title::text').get()
        }

