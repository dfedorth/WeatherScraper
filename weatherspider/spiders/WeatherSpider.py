# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import XMLFeedSpider


class WeatherspiderSpider(XMLFeedSpider):
    name = 'WeatherSpider'
    allowed_domains = ['forecast.weather.gov']
    url_template = "http://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}FcstType=digitalDWML"
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly
    target_latlons = [
        ("38.6889", "-121.088"),
    ]

    def start_requests(self):
        for (lat, lon) in target_latlons:
            yield Request(url_template.format(lat=lat, lon=lon))

    def parse_node(self, response, selector):
        i = {}
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
