# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         task
# Description:  
# Author:       Allen
# Time:         2021/1/12 13:27
# ------------------------------------------------------------------------------
from celery import Celery

app = Celery('demo', backend='redis://localhost:6379/1', broker='redis://localhost:6379/2')


@app.task
def add(x, y):
    return x + y
