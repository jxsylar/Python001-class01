# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import MaoyanMovieItem
from scrapy.exporters import CsvItemExporter


class MaoyanMoviePipeline:
    def open_spider(self, spider):
        filename = "maoyan_movie_scrapy_m.csv"
        f = open(filename, 'wb')
        self.exporter = CsvItemExporter(f)

    def process_item(self, item, spider):
        if type(item) == MaoyanMovieItem:
            self.exporter.export_item(dict(item))
            return item
