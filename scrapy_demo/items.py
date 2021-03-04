# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class OpticalLineItem(Item):
    url = Field()
    title = Field()
    date = Field()


class NewsItem(Item):
    title = Field()
    body = Field()
    time = Field()
