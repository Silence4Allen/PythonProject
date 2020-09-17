# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         process
# Description:  
# Author:       Allen
# Time:         2020/9/16 19:55
# -------------------------------------------------------------------------------
import random
import time
from multiprocessing import Process, Queue


def write(q):
    for value in ['A', 'B', 'C']:
        print(f"put {value} to queue")
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print(f"get {value} from queue")
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    q = Queue()
    w = Process(target=write, args=(q,))
    r = Process(target=read, args=(q,))
    w.start()
    w.join()
    r.start()

    r.join()
    # r.terminate()
    print("done")
