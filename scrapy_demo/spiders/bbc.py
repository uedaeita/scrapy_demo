# coding: utf-8

from datetime import datetime

from scrapy.spiders.sitemap import SitemapSpider
from scrapy.selector import Selector

from scrapy_demo.items import NewsItem


class BBCSpider(SitemapSpider):
    name = 'bbc'
    allowed_domains = ['www.bbc.com']
    sitemap_urls = [
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'https://www.bbc.com/sitemaps/https-sitemap-com-news-1.xml',
    ]
    sitemap_rules = [
        # 正規表現 '/news/' にマッチするページをparse_newsメソッドでパースする
        ('', 'parse_news'),
    ]

    def parse_news(self, response):
        item = NewsItem()

        sel = Selector(response)
        item['title'] = sel.xpath('//h1[@id="main-heading"]/text()').extract()
        item['body'] = u'\n'.join(
            u''.join(p.xpath('.//text()').extract()) for p in sel.css('article > p'))
        item['time'] = datetime.strptime(
            u''.join(sel.xpath('//time/@datetime').extract()),
            u'%Y-%m-%dT%H:%M:%S.%fZ')

        yield item
