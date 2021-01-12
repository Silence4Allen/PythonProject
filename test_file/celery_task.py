# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         celery_task
# Description:  
# Author:       Allen
# Time:         2021/1/12 10:34
# ------------------------------------------------------------------------------

"""
1.检查是否安装redis(由于我们采用redis来做broker)
2.启动redis-server
3.在工程目录下(test_file)执行命令: celery -A celery_task worker --loglevel=info 作为worker来消费
4.在该目录下执行python交互式编程
from celery_task import add
res = add.delay(1,2)
res.ready()可以查看结果是否处理完成
res.get()可以获取结果

注意：
broker是中间件，backend是结果保存
broker的配置一定是redis://localhost:6379/1，1这里只能是int，不能是字符串啥的，否则报错，backend同理
"""

from celery import Celery

celery_app = Celery('celery_task', broker='redis://localhost:6379/1', backend='redis://localhost:6379/2')


@celery_app.task
def add(x, y):
    print('call func')
    return x + y
