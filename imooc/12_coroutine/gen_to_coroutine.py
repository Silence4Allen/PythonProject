# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         gen_to_coroutine
# Description:  
# Author:       Allen
# Time:         2020/12/21 16:15
# ------------------------------------------------------------------------------
"""
 协程的调度依然是 事件循环+协程模式，协程是单线程模式
"""
import inspect


def gen_func():
    yield 1
    return "allen"


if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    print(next(gen))
    print(inspect.getgeneratorstate(gen))
    try:
        print(next(gen))
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))
