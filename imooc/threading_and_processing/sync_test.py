# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         sync_test
# Description:  
# Author:       Allen
# Time:         2020/12/20 10:44
# ------------------------------------------------------------------------------
"""
加锁可以避免线程之间通信数据出现问题
但是加锁后一定要记得释放锁
Lock对象不能连续两次acquire()，而RLock可以在同一线程里面，多次调用acquire()，但是需要注意释放release()的次数一定要等于获得锁的次数
锁带来的问题有：
a.降低性能
b.可能造成死锁
"""
from threading import Lock, RLock

total = 0
lock = Lock()
r_lock = RLock()


def add():
    global total, lock, r_lock
    for i in range(1000000):
        # lock.acquire()
        r_lock.acquire()
        r_lock.acquire()
        total += 1
        # lock.release()
        r_lock.release()
        r_lock.release()


def desc():
    global total, lock, r_lock
    for i in range(1000000):
        r_lock.acquire()
        total -= 1
        r_lock.release()


import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
