# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         call_test
# Description:  
# Author:       Allen
# Time:         2020/12/22 11:44
# ------------------------------------------------------------------------------

import asyncio


def callback(sleep_times, loop):
    print("success time {}".format(loop.time()))


def stop_loop(loop):
    loop.stop()


# call_later,call_at,call_soon
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now + 2, callback, 9, loop)
    loop.call_later(2, callback, 2, loop)
    loop.call_later(1, callback, 1, loop)
    loop.call_later(3, callback, 3, loop)
    loop.call_soon(callback, 4, loop)
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()
