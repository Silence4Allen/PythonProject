# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         python_thread
# Description:  
# Author:       Allen
# Time:         2020/12/19 14:20
# ------------------------------------------------------------------------------
"""
进程-->线程
对于io操作来说，多线程和多进程性能不大

"""
import threading
import time


def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print('get detail url started')
    time.sleep(4)
    print("get detail url end")


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail html started')
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(4)
        print("get detail url end")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # thread1.setDaemon(True)
    thread2.setDaemon(True)  # 设置成守护线程，守护线程会在主进程代码执行结束后就终止
    start_time = time.time()
    thread1.start()
    thread2.start()

    # thread1.join()
    # thread2.join()
    print("last time:{}".format(time.time() - start_time))

    thread1 = GetDetailHtml('get_detail_html')
    thread2 = GetDetailUrl('get_detail_url')
    start_time = time.time()
    thread1.start()
    thread2.start()
