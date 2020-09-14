# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         closure
# Description:  
# Author:       Allen
# Time:         2020/9/1 20:09
# -------------------------------------------------------------------------------
import time


def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(args)
        end_time = time.perf_counter()
        print(end_time - start_time)

    return wrapper


class Closure(object):

    @time_counter
    def do(self):
        for i in range(3):
            print(i)
            time.sleep(1)
        print("done")


if __name__ == '__main__':
    c = Closure()
    c.do()
