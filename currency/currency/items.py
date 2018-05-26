# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CurrencyItem(Item):
    # fields
    from_currency = Field()
    date = Field()
    name = Field()
    rate = Field()
    url = Field()

