# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test
# Description:  
# Author:       Allen
# Time:         2020/9/14 19:21
# -------------------------------------------------------------------------------
import time


def time_counter(func):
    def wrapper():
        start_time = time.process_time()
        func()
        end_time = time.process_time()
        print(end_time - start_time)

    return wrapper


@time_counter
def do():
    for i in range(3):
        print(i)
        time.sleep(1)
    print("done")


do()
