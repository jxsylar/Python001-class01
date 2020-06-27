# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql


class MysqlPipeline():
    def __init__(self, host, database, table, user, password, port):
        self.host = host
        self.database = database
        self.table = table
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            table=crawler.settings.get('MYSQL_TABLE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        sql_fmt = """INSERT INTO `{}`(`movie_id`, `name`, `score`, `url`, `poster`, `info`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');"""
        sql = sql_fmt.format(self.table,
                             item['movie_id'], item['name'],
                             item['score'], item['url'],
                             item['poster'], json.dumps(item['info'], ensure_ascii=False),
                             )
        self.cursor.execute(sql)
        self.db.commit()
        return item
