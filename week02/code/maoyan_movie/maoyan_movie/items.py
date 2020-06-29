# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class MaoyanMovieItem(Item):
    movie_id = Field()
    name_cn = Field()
    name_en = Field()
    type = Field()
    show_time = Field()
    score = Field()
    avatar = Field()
