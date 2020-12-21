# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         async_await
# Description:  
# Author:       Allen
# Time:         2020/12/21 16:31
# ------------------------------------------------------------------------------

# python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程
import types


@types.coroutine
def downloader2(url):
    yield 'allen'


async def downloader(url):
    return "allen"


async def download_url(url):
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = download_url('http://www.baidu.com')
    coro.send(None)
