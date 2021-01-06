# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         http_client
# Description:  
# Author:       Allen
# Time:         2021/1/4 11:41
# ------------------------------------------------------------------------------
# 同步函数
import asyncio

from tornado.httpclient import HTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


from tornado.gen import Runner
# 异步+回调函数
from tornado.httpclient import AsyncHTTPClient


def asynchronous_fetch(url, callback):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        callback(response.body)

    http_client.fetch(url, callback=handle_response)


# 通过future替代回调函数
from tornado.concurrent import Future


def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result())
    )
    return my_future


# 协程
from tornado import gen


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    # 在 Python 3.3 之前的版本中, 从生成器函数
    # 返回一个值是不允许的,你必须用
    #   raise gen.Return(response.body)
    # 来代替
    return response.body


# python3.5后引入async和await关键字来替代yield和@gen.coroutine装饰器
async def fetch_coroutine_use_async(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    res = fetch_coroutine(url)
    pass
