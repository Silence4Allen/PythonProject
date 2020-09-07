# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         closure
# Description:  
# Author:       Allen
# Time:         2020/9/1 20:09
# -------------------------------------------------------------------------------
import time


class Closure(object):

    def time_counter(self, func):
        def wrapper():
            start_time = time.clock()
            func()
            end_time = time.clock()
            print(end_time - start_time)

        return wrapper()

    @time_counter
    def do(self):
        for i in range(1000):
            pass
        print("done")


if __name__ == '__main__':
    def time_counter(func):
        def wrapper():
            start_time = time.clock()
            func()
            end_time = time.clock()
            print(end_time - start_time)

        return wrapper()


    @time_counter
    def do():
        for i in range(1000):
            pass
        print("done")

    do()