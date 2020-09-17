# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         pool
# Description:  
# Author:       Allen
# Time:         2020/9/16 20:16
# -------------------------------------------------------------------------------
import os
import random
import time
from multiprocessing import Pool


def worker(msg):
    t_start = time.perf_counter()
    print(f"开始执行, msg={msg}, 进程号为{os.getpid()}")
    time.sleep(random.random() * 5)
    t_end = time.perf_counter()
    print(f"---进程号为{os.getpid()}, 耗时{(t_start - t_end) * 5}---")


if __name__ == '__main__':
    ps = Pool(3)
    for i in range(10):
        ps.apply_async(worker, (i,))
    print("start")
    ps.close()
    ps.join()
    print("done")
