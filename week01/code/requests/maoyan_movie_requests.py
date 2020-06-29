#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-06-25 16:01:25

"""
requests 版本
"""

import csv
import time

import requests
from furl import furl
from parsel import Selector

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'text/plain, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593071575,1593071665,1593071730,1593074417; _lxsdk_cuid=172e9578d9fa8-090927fc871c2d-376b4502-1fa400-172e9578da0c8; _lxsdk=922FF590B88111EAA1F189776DB49E05F99C6E83AF29404581A9B8FFB1A3AA86; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593430757; __mta=44389915.1593267725645.1593267850174.1593430757827.4; _lxsdk_s=172ffdfce9b-3b9-0eb-5e3%7C%7C2; uuid_n_v=v1; iuuid=451797E0B9FD11EAA91D41CC1BE79A36DC721E79AA674189B10EEC240568152A; webp=true; ci=50%2C%E6%9D%AD%E5%B7%9E; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172ffe08ace1d6-05b9eea18d0a5-2d604637-304500-172ffe08acf262%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172ffe08ace1d6-05b9eea18d0a5-2d604637-304500-172ffe08acf262%22%7D'
}

base_url = "https://m.maoyan.com/ajax/moreClassicList"

params = {
    'sortId': '1',
    'showType': '3',
    'limit': 100,
    'offset': 0,
    'optimus_uuid': '451797E0B9FD11EAA91D41CC1BE79A36DC721E79AA674189B10EEC240568152A',
    'optimus_risk_level': '71',
    'optimus_code': '10'
}


def get_html(f_url: furl):
    response = requests.get(f_url.url, headers=headers)
    html = response.text
    return html


def parse_movie(html):
    sel = Selector(text=html)
    for a in sel.css("body > a"):
        movie_id = a.re_first(r"\d+")
        div = a.css("div.classic-movie")
        avatar = div.css("div.avatar img::attr(src)").get()
        name_cn = div.css("div.movie-info div.title::text").get()
        name_en = div.css("div.movie-info div.english-title::text").get()
        type_ = div.css("div.movie-info div.actors::text").get()
        show_time = div.css("div.movie-info div.show-info::text").get()
        score = div.css("div.movie-score div.score span.grade::text").get()
        no_score = div.css("div.movie-score div.no-score::text").get()
        movie = {
            '_id': movie_id,
            'name_cn': name_cn,
            'name_en': name_en,
            'type': type_,
            'show_time': show_time,
            'score': score or no_score,
            'avatar': avatar,
        }
        yield movie


def crawl(writer):
    count = 0
    f_url = furl(base_url).add(params)
    html = get_html(f_url)
    while True:
        for item in parse_movie(html):
            count += 1
            writer.writerow(item)
        f_url.args['offset'] += f_url.args['limit']
        time.sleep(5)
        html = get_html(f_url)
        if count >= 200:
            break


def main():
    out_file = 'maoyan_movie_requests_m.csv'
    with open(out_file, 'w', encoding='utf-8') as _f:
        fieldnames = ['_id', 'name_cn', 'name_en', 'type', 'show_time', 'score', 'avatar']
        writer = csv.DictWriter(_f, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        crawl(writer)


if __name__ == '__main__':
    main()
