# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         progress_queue
# Description:  
# Author:       Allen
# Time:         2020/12/20 16:17
# ------------------------------------------------------------------------------
"""
共享全局变量不能适用于多进程编程，可以适用于多线程
"""
import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe


def producer(queue):
    queue.put('a')
    time.sleep(2)


def consumer(queue):
    time.sleep(3)
    data = queue.get()
    print(data)


def producer_by_pipe(pipe):
    pipe.send('allen')
    time.sleep(2)


def consumer_by_pipe(pipe):
    time.sleep(3)
    data = pipe.recv()
    print(data)


def add_data(d, k, v):
    d[k] = v


if __name__ == '__main__':
    queue = Queue(10)
    p = Process(target=producer, args=(queue,))
    c = Process(target=consumer, args=(queue,))
    p.start()
    c.start()
    p.join()
    c.join()

    # ***注意***：上述的queue不能用于进程池通信，需要使用Manager对象的Queue()方法，多个进程可以共享一个queue
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))
    pool.close()
    pool.join()

    # 使用Pipe管道通信，但是Pipe只能适用于两个进程间的通信，pipe性能高于queue
    receive_pipe, send_pipe = Pipe()
    p = Process(target=producer_by_pipe, args=(send_pipe,))
    c = Process(target=consumer_by_pipe, args=(receive_pipe,))
    p.start()
    c.start()
    p.join()
    c.join()

    # 进程通过共享变量（Manager下面的数据类型）
    d = Manager().dict()
    f_p = Process(target=add_data, args=(d, "k1", "v1"))
    s_p = Process(target=add_data, args=(d, "k2", "v2"))
    f_p.start()
    s_p.start()
    f_p.join()
    s_p.join()
    print(d)
