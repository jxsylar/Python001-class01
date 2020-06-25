# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class MaoyanMovieItem(Item):
    _id = Field()
    name = Field()
    score = Field()
    url = Field()
    poster = Field()
    info = Field()
