from scrapy import Spider
from scrapy.selector import Selector
from scrapy_currency.items import ScrapyCurrencyItem
from datetime import datetime


class CurrencySpider(Spider):
    name = "scrapy_currency"
    allowed_domains = ["x-rates.com"]
    start_urls = [
        # "http://stackoverflow.com/questions?pagesize=50&sort=newest",
        # additional parameter date, format Y-m-d, ex: 1999-03-26
        "https://x-rates.com/historical/?from=USD&amount=1",
        "https://x-rates.com/historical/?from=EUR&amount=1",
        "https://x-rates.com/historical/?from=GBD&amount=1",
        "https://x-rates.com/historical/?from=INR&amount=1",
        "https://x-rates.com/historical/?from=AUD&amount=1",
        "https://x-rates.com/historical/?from=CAD&amount=1",
        "https://x-rates.com/historical/?from=SGD&amount=1",
        "https://x-rates.com/historical/?from=CHF&amount=1",
        "https://x-rates.com/historical/?from=MYR&amount=1",
        "https://x-rates.com/historical/?from=JPY&amount=1",
        "https://x-rates.com/historical/?from=CNY&amount=1"
    ]

    def parse(self, response):
        # Priority order xpath
        # currencies = Selector(response).xpath('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr')
        # Alphabetical order xpath
        currencies = Selector(response).xpath('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr')

        from_currency = ''
        date = ''
        params = response.url.split("?")[1].split("&")
        for param_item in params:
            param = param_item.split("=")
            if param[0] == 'from':
                from_currency = param[1]
            elif param[0] == 'date':
                date = param[1]

        for currency in currencies:
            item = ScrapyCurrencyItem()
            item['from_currency'] = from_currency
            item['date'] = datetime.strptime(date, '%Y-%m-%d')
            item['name'] = currency.xpath('td[1]/text()').extract()[0]
            item['rate'] = currency.xpath('td[2]/a/text()').extract()[0]
            item['url'] = currency.xpath('td[2]/a/@href').extract()[0]
            yield item

