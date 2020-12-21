# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         progress_test
# Description:  
# Author:       Allen
# Time:         2020/12/20 15:27
# ------------------------------------------------------------------------------
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    # 1.对于耗费cpu的操作，多进程优于多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("execute result :{}".format(data))
    #     print("cost time is :{}".format(time.time() - start_time))
    #
    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("execute result :{}".format(data))
    #     print("cost time is :{}".format(time.time() - start_time))

    # 2.对于耗费cpu的操作，多线程优于多进程
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("execute result :{}".format(data))
        print("cost time is :{}".format(time.time() - start_time))

    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("execute result :{}".format(data))
        print("cost time is :{}".format(time.time() - start_time))
