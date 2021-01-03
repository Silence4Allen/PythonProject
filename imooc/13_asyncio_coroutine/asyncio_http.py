# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         asyncio_http
# Description:  模拟http请求
# Author:       Allen
# Time:         2020/12/22 12:10
# ------------------------------------------------------------------------------
# asyncio 没有提供http协议的接口,aiohttp

import asyncio
import socket
from urllib.parse import urlparse


async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'
    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, port=80)
    writer.write('GET {} HTTP/1.1\r\nHOST:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode('utf8')
        all_lines.append(data)
    html = '\n'.join(all_lines)
    return html


async def main():
    tasks = []
    for url in ['http://www.baidu.com']:
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
