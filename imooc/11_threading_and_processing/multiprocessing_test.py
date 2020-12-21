# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         multiprocessing_test
# Description:  
# Author:       Allen
# Time:         2020/12/20 15:46
# ------------------------------------------------------------------------------
import multiprocessing
import os
import time


# print('hello')
# pid = os.fork()
# print('allen')
# if pid == 0:
#     print("pid:{}".format(pid))
#     print("子进程:{}, 父进程:{}".format(os.getpid(), os.getppid()))
# else:
#     print("我是父进程:{}".format(pid))
# time.sleep(2)

import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print("sub process end")
    return n


if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(3,))
    process.start()
    print(process.pid)
    process.join()
    print("main process end")

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3,))
    # 不接收新的子进程任务
    pool.close()
    # 等待所有任务完成
    pool.join()
    print(result.get())

    for result in pool.imap(get_html, [2, 4, 5, 1]):
        print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [2, 4, 5, 1]):
        print("{} sleep success".format(result))
