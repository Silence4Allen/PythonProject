# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         queue_test
# Description:  
# Author:       Allen
# Time:         2020/12/20 10:27
# ------------------------------------------------------------------------------
from queue import Queue

total = 0


def add(q):
    for i in range(10):
        q.put(i)


def desc(q):
    for i in range(10):
        n = q.get(i)
        print(n)
        q.task_done()


import threading

q = Queue(maxsize=5)

thread1 = threading.Thread(target=add, args=(q,))
thread2 = threading.Thread(target=desc, args=(q,))
thread1.start()
thread2.start()

thread1.join()
thread2.join()


if q.all_tasks_done:
    print("is_empty2:{}".format(q.empty()))
q.join()
print("is_empty1:{}".format(q.empty()))