# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         main
# Description:  
# Author:       Allen
# Time:         2021/1/12 14:12
# ------------------------------------------------------------------------------
from celery_study import task_add

task_add.add.delay(8, 4)
print('end...')
