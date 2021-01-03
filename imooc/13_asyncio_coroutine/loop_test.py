# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         loop_test
# Description:  
# Author:       Allen
# Time:         2020/12/22 10:36
# ------------------------------------------------------------------------------
"""
事件循环+回调（驱动生成器）+epoll（IO多路复用）
asyncio是python用于解决异步io编程的一整套方案
tornado、gevent、twisted（scrapy,django channels）
tornado（实现web服务器），django+flask（uwsgi，gunicorn+ngiinx）
tornado可以直接部署。nginx+tornado
"""

import asyncio
import time
from functools import partial


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return 'hello'


def callback(url, future):
    print(url)
    print('send email to allen')


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    start_time = time.time()
    loop = asyncio.get_event_loop()

    # 1.多个任务
    # tasks = [get_html(url) for i in range(1000)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # 2
    # tasks = [get_html(url) for i in range(1000)]
    # loop.run_until_complete(asyncio.gather(*tasks))

    # 3
    # get_future = asyncio.ensure_future(get_html(url))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # 4
    # task = loop.create_task(get_html(url))
    # # task.add_done_callback(callback)
    # task.add_done_callback(partial(callback, url))
    # loop.run_until_complete(task)
    # print(task.result())

    group1 = [get_html(url) for i in range(2)]
    group2 = [get_html(url) for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))

    print(time.time() - start_time)
