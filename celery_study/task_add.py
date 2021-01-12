# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         task_add
# Description:  
# Author:       Allen
# Time:         2021/1/12 14:05
# ------------------------------------------------------------------------------
import time
from celery_study import app


@app.task
def add(x, y):
    time.sleep(3)
    return x + y
