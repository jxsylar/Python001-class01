# week01 学习笔记

本周主要学习了如何使用 requests 和 scrapy 从网页中爬取数据.

爬虫最主要作用就是模拟客户端(如浏览器)向服务器发送请求, 从而收集获取网页上的信息. 为了顺利完成这一过程, 基本需要掌握:

1. HTTP 基本原理
2. WEB 网页基础, 如 HTML, css, js
3. 使用具体的编程语言完成发请求(request), 解析返回的响应数据(xpath, css), 以及后续的数据存储等过程

## 关于解析数据

1. 发送请求后得到的响应数据, 如果是 HTML 源码的, 建议使用 xpath 或 css 选择器来解析数据, 因为 xpath 和 css 选择器能够在 Chrome 浏览器开发者工具 Elements 选项卡里 `Ctrl + F` 能够直接使用, 方便调试, 而且效率比 BeautifulSoup 快很多;
2. 强烈不建议使用浏览器开发者工具 Elements 选项卡 `copy xpath` 的功能, 因为复制得到的 xpath **不健壮**, 建议结合 HTML 节点特征进行自行编写 xpath. 不过在初学时还是建议使用 `copy xpath` 以加快对 xpath 的认识, 但后面得摆脱它;
3. 在 Elements 里测试 xpath 或 css 选择器时, 一定要先检查网页源码和 Elements 里看到的内容是不是一模一样, 否则辛辛苦苦编写的 xpath 或 css 选择器直接报废了;

## 关于 scrapy

1. scrapy 的功能可以说是非常强大, 所以如果想要用好 scrapy, 就要深入了解各个组件的功能以及使用方法, 中间件和插件机制非常容易拓展 scrapy 的功能.
2. 在 spiders 的每个爬虫里, response 对象[自带有 xpath, css, re 的功能](https://docs.scrapy.org/en/latest/topics/selectors.html), 而不需要额外引入第三方库.
3. scrapy 选择器在底层其实是[对  parsel 库的二次封装](https://docs.scrapy.org/en/latest/topics/selectors.html), 所以, 在不使用 scrapy 时, 想要拥有和 response 对象选择器一样的功能, 就可以使用 parsel 这个库, 使用方式与 response 几乎一模一样
4. scrapy 自带一个很好的调试功能: [scrapy shell](https://docs.scrapy.org/en/latest/topics/shell.html)

## 作业中遇到的问题以及解决方案


1. 在爬取猫眼电影时, 发送请求时, 并不像豆瓣 TOP250 那么顺利, 会遇到反爬, 主要解决思路:

- headers 把 cookies 也要加上, cookies 的有效期还是比较长的, 短时间内使用是没问题的
- 控制一下请求频率, 如果出现需要验证码, 短期内可以在日志文件里将验证的 URL 复制到浏览器完成验证

2. scrapy item pipeline 里, [自带有序列化输出文件的类](https://docs.scrapy.org/en/latest/topics/feed-exports.html), 支持 json, jsonline, csv, xml 这 4 中格式, 在 pipeline 里可以直接使用. 当然, 完全可以使用自己实现的方式进行数据保存.
