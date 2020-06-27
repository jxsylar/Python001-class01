# -*- coding: utf-8 -*-
import json

import scrapy
from twisted.python.failure import Failure

from ..items import MaoyanMovieItem


class MaoyanMovieSpider(scrapy.Spider):
    name = 'crawl_maoyan_movie'
    allowed_domains = ['maoyan.com']

    def __init__(self):
        self.headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'uuid_n_v=v1; uuid=922FF590B88111EAA1F189776DB49E05F99C6E83AF29404581A9B8FFB1A3AA86; _csrf=e02fd6917a889a2abd8ee26f0c45f78557d0f1ff00bf3ae4a2de87f17e3a815a; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593071575,1593071665,1593071730,1593074417; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593267725; _lxsdk_cuid=172e9578d9fa8-090927fc871c2d-376b4502-1fa400-172e9578da0c8; _lxsdk=922FF590B88111EAA1F189776DB49E05F99C6E83AF29404581A9B8FFB1A3AA86; mojo-uuid=bffd4a534711b42d9c8a3c961673a0d2; mojo-session-id={"id":"7e915bd24e819739d43a6e4bc7cf5e4a","time":1593267725629}; mojo-trace-id=1; __mta=44389915.1593267725645.1593267725645.1593267725645.1; _lxsdk_s=172f6281cef-8da-3a8-ac9%7C%7C3'
        }

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3&offset=0'
        # 增加错误回调函数
        yield scrapy.Request(url, headers=self.headers, errback=self.errback)

    def parse(self, response):
        self.logger.info(f"proxy: {response.meta['proxy']}")
        if 'verify' not in response.url:
            dd = response.xpath("//div[@class='movies-list']/dl[@class='movie-list']/dd")
            # html 中 <dd> 没有闭合标签, 使用 Selector 后, 自动补上 </dd>, 但每个 <dd> 标签已不是并列的, 而是层层嵌套
            while True:
                movie_item = dd.xpath("div[contains(@class, 'movie-item')]")
                movie_id = movie_item.xpath("a/@data-val").re_first(r"\d+")
                movie_url = f"https://maoyan.com/films/{movie_id}"
                # poster = movie_item.xpath("a/div[@class='movie-poster']/img[last()]/@data-src").get()  # 160*220
                poster = movie_item.xpath("div[@class='movie-item-hover']/a/img/@src").get()  # 218*300

                name = dd.xpath("div[contains(@class, 'movie-item-title')]/@title").get()
                score = dd.xpath("div[contains(@class, 'channel-detail channel-detail-orange')]//text()").getall()
                score = ''.join(score)

                # 类型, 主演, 上映时间
                info = {}
                for div in movie_item.xpath("div[@class='movie-item-hover']//div[@class='movie-hover-info']/div")[1:]:
                    t = div.xpath(".//text()").getall()
                    t = [i.strip() for i in t if i and i.strip()]
                    t = ''.join(t)
                    k, v = t.split(':', 1)
                    info.update({k: v})

                item = MaoyanMovieItem()
                item['movie_id'] = movie_id
                item['name'] = name
                item['score'] = score
                item['info'] = info
                item['url'] = movie_url
                item['poster'] = poster
                yield item

                dd = dd.xpath('./dd')
                if not dd:
                    break

    def errback(self, failure: Failure):
        """
        https://docs.scrapy.org/en/latest/topics/request-response.html
        https://docs.scrapy.org/en/latest/topics/request-response.html#topics-request-response-ref-errbacks
        :param failure:
        :return:
        """
        request = failure.request
        url = request.url
        _id = request.meta.get('_id', '')
        res = {
            '_id': _id,
            'url': url,
            'error_type': f"{failure.type}",
            'msg': failure.getErrorMessage(),
            'traceback': failure.getBriefTraceback(),
        }
        try:
            status = failure.value.response.status
            res.update({'status': status})
        except:
            pass

        self.logger.error(json.dumps(res, ensure_ascii=False))
