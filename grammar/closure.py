# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         closure
# Description:  
# Author:       Allen
# Time:         2020/9/1 20:09
# -------------------------------------------------------------------------------
import time


def time_counter(func, *args, **kwargs):
    print(args)
    print(**kwargs)

    def wrapper(*args, **kwargs):
        print(args)
        print(**kwargs)
        start_time = time.perf_counter()
        func(args)
        end_time = time.perf_counter()
        print(end_time - start_time)

    return wrapper


type(1)


class Closure(ValueError, object):
    # def time_parent(self):

    # return time_counter
    # time_counter(print("print"))

    @time_counter
    def do(self):
        for i in range(3):
            print(i)
            time.sleep(1)
        print("done")


if __name__ == '__main__':
    c = Closure()
    # c.do()
    print(type(1))
    print(type(c))
    print(type(Closure))
    print(type(Closure.__bases__))
    print(Closure.__bases__)
    print(type(object))
    print(type(type))
