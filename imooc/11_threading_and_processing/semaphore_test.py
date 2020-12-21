# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         semaphore_test
# Description:  
# Author:       Allen
# Time:         2020/12/20 13:52
# ------------------------------------------------------------------------------
"""
Semaphore是用于控制进入数量的锁，可以控制线程的并发数量
文件读写，写一般只是用于一个线程写，读可以允许多个
"""
import threading
import time


class Spider(threading.Thread):
    def __init__(self, url, sem):
        super(Spider, self).__init__()
        self.url = url
        self.sem = sem

    def run(self) -> None:
        time.sleep(2)
        print("got html detail success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(10):
            self.sem.acquire()
            spider = Spider("http://www.baidu.com/{}".format(i), self.sem)
            spider.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
