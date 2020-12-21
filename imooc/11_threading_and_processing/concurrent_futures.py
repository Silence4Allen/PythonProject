# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         concurrent_futures
# Description:  
# Author:       Allen
# Time:         2020/12/20 14:10
# ------------------------------------------------------------------------------
"""
线程池，为什么要有线程池？
主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
当一个线程完成的时候我们主线程能立即知道
futures可以让多线程和多进程编码接口一致
"""
import time



def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池,submit非阻塞，立马返回
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# cancel可以取消任务，执行中的不可以取消
task2.cancel()
# done方法可以判定是否完成
print(task1.done())

time.sleep(4)
print(task1.done())
# result方法可以获取返回结果
print(task1.result())

# 要获取已经成功的task
# method 1
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print("main1")
for future in as_completed(all_task):
    data = future.result()
    print("get {} page".format(data))

# method 2
# for data in executor.map(get_html, urls):
#     print("get {} page".format(data))

print("main2")
