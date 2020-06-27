# -*- coding: utf-8 -*-
import random


class ProxyMiddleware:
    def __init__(self):
        """代理样例, 由于本项目一定是 https, 所以这里简单使用.
        生产环境中, 都是调用接口获取代理, 为了能在 scrapy 中间件和其他代码中使用,
        会单独封装一个类用于获取代理, 然后在不同的使用场景中进行适配.
        """
        self.proxies = [
            'https://183.141.63.219:4236',
            'https://221.1.124.51:4284',
            'https://125.86.166.232:4237',
        ]

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.meta['proxy'] = random.choice(self.proxies)

